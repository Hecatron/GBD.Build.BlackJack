from .opts.GenerateOpts import GenerateOpts
import blackjack.contrib.pexpect.wexpect as pexpect
import sys, time, os, shutil

class CMakeInfo(object):
    """Access cmake related information"""

    def __init__(self, opts:GenerateOpts = None):
        self.Opts = opts
        """Options for generating cmake / make build files"""
        if self.Opts is None: self.Opts = GenerateOpts()

        self.Version = None
        """Version of cmake discovered"""

        self.Generators = None
        """List of generators supported by cmake discovered"""

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
