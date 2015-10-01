from .ProcessOpts import ProcessOpts
import blackjack.contrib.pexpect.wexpect as pexpect
import sys, time, os, shutil

class CMakeProcess(object):
    """Represents a cmake Process that can be called externally"""

    def __init__(self, opts:ProcessOpts = None):
        self.Opts = opts
        """Options for launching cmake"""
        if self.Opts is None: self.Opts = ProcessOpts()

        self.Process = None
        """Active cmake process that is running"""

        self.Version = None
        """Version of cmake discovered"""

        self.Generators = None
        """List of generators supported by cmake discovered"""
        return

    def run(self):
        """Start the running of cmake"""
        workdir = self.Opts.BuildDirectory
        if workdir is not None:
            if os.path.exists(workdir):
                if os.path.isdir(workdir) == False: raise ValueError("Build Directory is invalid")
            else:
                os.makedirs(workdir)

        # TODO options
        cmdargs = self.Opts.get_opts()
        self.Process = pexpect.spawn(self.Opts.CMakeBinPath, args = cmdargs, cwd = workdir)
        self.Process.logfile = self.Opts.LogFile
        if self.Process.isalive: self.Process.wait()
        self.Process.expect(pexpect.EOF)
        self.Process.close()
        return

    def clean(self):
        """Clean the build directory / cmake cache"""
        if self.Opts is not None:
            if self.Opts.BuildDirectory is not None:
                shutil.rmtree(self.Opts.BuildDirectory, ignore_errors=True)
        return

    def get_generators(self):
        """Get a list of generators"""
        child = pexpect.spawn(self.Opts.CMakeBinPath, ["--help"])
        time.sleep(0.5)
        child.expect('The following generators are available on this platform:')
        child.expect(pexpect.EOF)
        child.close()
        result = child.before.replace('\r', '')
        result = result.split("\n")
        resultlist = list()
        for item in result:
            if item == '': continue
            if "=" in item:
                itemsplit = item.split("=")
                itemsplit[0] = itemsplit[0].replace("[arch]", "").strip()
                itemsplit[1] = itemsplit[1].strip()
                resultlist.append([itemsplit[0],itemsplit[1]])
            else:
                resultlist[-1][1] += "\n" + item.strip()

        self.Generators = resultlist
        return self.Generators

    def get_version(self):
        """Get the Version of CMake"""
        child = pexpect.spawn(self.Opts.CMakeBinPath, ["--version"])
        child.expect('cmake version ')
        child.expect(pexpect.EOF)
        child.close()
        result = child.before.split('\n')[0]
        result = result.replace('\r', '')
        self.Version = result
        return self.Version

    def testexe(self):
        """Test the cmake exe"""
        # Test the CMake exe
        child = pexpect.spawn(self.Opts.CMakeBinPath, ["--version"])
        # Log everything to stdout
        child.logfile = sys.stdout
        # Tell pexpect to finish processing
        child.expect(pexpect.EOF)
        child.close()
        result = child.before
        return result
