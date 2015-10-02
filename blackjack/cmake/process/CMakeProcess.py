from .opts.BuildOpts import BuildOpts
from .opts.GenerateOpts import GenerateOpts
import blackjack.contrib.pexpect.wexpect as pexpect
import sys, time, os, shutil

class CMakeProcess(object):
    """Represents a cmake Process that can be called externally"""

    def __init__(self, opts:GenerateOpts = None, buildopts:BuildOpts = None):
        self.Opts = opts
        """Options for generating cmake / make build files"""
        if self.Opts is None: self.Opts = GenerateOpts()

        self.BuildOpts = buildopts
        """Options for lunching cmake in build mode"""
        if self.BuildOpts is None: self.BuildOpts = BuildOpts()

        self.Process = None
        """Active cmake process that is running"""
        return

    def generate(self):
        """Start the running of cmake to generate the build files"""
        self.setupworkingdir(self.Opts.BuildDirectory)
        cmdargs = self.Opts.get_opts()
        self.Process = pexpect.spawn(self.Opts.CMakeBinPath, args = cmdargs, cwd = self.Opts.BuildDirectory)
        self.Process.logfile = self.Opts.LogFile
        if self.Process.isalive: self.Process.wait()
        self.Process.expect(pexpect.EOF)
        self.Process.close()
        
        self.BuildOpts.CMakeBinPath = self.Opts.CMakeBinPath
        self.BuildOpts.BuildDirectory = self.Opts.BuildDirectory
        return

    def build(self):
        """Use cmake to start the build process"""
        self.setupworkingdir(self.BuildOpts.BuildDirectory)
        cmdargs = self.BuildOpts.get_opts()
        self.Process = pexpect.spawn(self.BuildOpts.CMakeBinPath, args = cmdargs, cwd = self.BuildOpts.BuildDirectory)
        self.Process.logfile = self.BuildOpts.LogFile
        #if self.Process.isalive: self.Process.wait()
        self.Process.expect(pexpect.EOF)
        self.Process.close()
        return

    def clean(self):
        """Clean the build directory / cmake cache"""
        if self.Opts is not None:
            if self.Opts.BuildDirectory is not None:
                shutil.rmtree(self.Opts.BuildDirectory, ignore_errors=True)
        return

    def setupworkingdir(self, workdir):
        """Check the working directory exists"""
        if workdir is not None:
            if os.path.exists(workdir):
                if os.path.isdir(workdir) == False: raise ValueError("Build Directory is invalid")
            else:
                os.makedirs(workdir)
        return
