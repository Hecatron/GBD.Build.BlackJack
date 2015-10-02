import sys

class BaseOpts(object):
    """Base class for cmake related options"""

    def __init__(self, cmakepath:str = None):
        # Exe suffix for windows
        self.ExeSuffix = ""
        if sys.platform == 'win32': self.ExeSuffix = ".exe"
        
        # Assume cmake is in the current path
        self.CMakeBinPath = "cmake" + self.ExeSuffix
        """Binary path to the cmake executable"""
        if cmakepath is not None: self.CMakePath = cmakepath
        
        self.BuildDirectory = None
        """Directory where the output from running cmake will be placed"""
        
        self.LogFile = sys.stdout
        """Log destination when running cmake"""

        self.Args = list()
        """Last set of options created during get_opts"""
        return

    def get_opts(self):
        """Virtual Member"""
        return
