from .BaseOpts import BaseOpts

class GenerateOpts(BaseOpts):
    """Command line options passed to a cmake process during generation"""

    def __init__(self, cmakepath:str = None):
        super().__init__(cmakepath = cmakepath)

        self.SourceDirectory = None
        """Directory where the CMakeLists.txt files will be sourced"""

        self.CachePreload = None
        """Pre-load a script to populate the cache."""

        self.Defines = list()
        """Defines cmake cache entries"""

        self.ToolChainFile = None
        """If to load in a toolchain file to override the toolchain settings"""

        self.GlobbingRemoveExpr = list()
        """Remove matching entries from CMake cache"""

        self.Generator = None
        """Which generator to use when creating the make build files"""

        self.ToolsetName = None
        """Specify toolset name if supported by generator"""

        self.PlatformName = None
        """Specify platform name if supported by generator"""

        self.SuppressDevelWarns = False
        """Suppress developer warnings"""

        self.EnableDevelWarns = False
        """Enable developer warnings"""

        self.ViewMode = False
        """View mode only"""

        self.ProcessScriptMode = None
        """Process the given cmake file as a script written in the CMake language
        No configure or generate step is performed and the cache is not modified"""

        self.Debug_TryCompile = False
        """Do not delete the try_compile build tree"""

        self.Debug_Output = False
        """Put cmake in a debug mode"""

        self.Debug_Trace = False
        """Put cmake in trace mode"""

        self.Debug_WarnUninit = False
        """Warn about uninitialized values"""

        self.Debug_WarnUnusedVars = False
        """Warn about unused variables"""

        self.Debug_NoWarnUnusedCli = False
        """Don't warn about command line options"""

        self.CheckSystemVars = False
        """Find problems with variable usage in system files"""


    def get_opts(self):
        """Generate cmd line opts for generate mode"""
        # The Build directory is used as the working directory when running cmake in generate mode
        self.Args = list()

        if self.CachePreload is not None: 
            self.Args.append("-C" + str(self.CachePreload))
        
        # Add the list of defines / toolchain file if specified
        deflist = list(self.Defines)
        if self.ToolChainFile is not None: 
            deflist.append("CMAKE_TOOLCHAIN_FILE=" + self.ToolChainFile)
        for item in deflist:
            if isinstance(item, str):
                self.Args.append("-D" + item)
        
        # TODO Cache variables

        for item in self.GlobbingRemoveExpr:
            self.Args.append("-U" + str(item))
        if self.Generator is not None: 
            self.Args.append("-G" + str(self.Generator))
        if self.ToolsetName is not None:
            self.Args.append("-T" + str(self.ToolsetName))
        if self.PlatformName is not None:
            self.Args.append("-A" + str(self.PlatformName))
        if self.SuppressDevelWarns:
            self.Args.append("-Wno-dev")
        if self.EnableDevelWarns:
            self.Args.append("-Wdev")
        if self.ViewMode:
            self.Args.append("-N")
        if self.ProcessScriptMode is not None:
            self.Args.append("-P" + str(self.ProcessScriptMode))
        if self.Debug_TryCompile:
            self.Args.append("--debug-trycompile")
        if self.Debug_Output:
            self.Args.append("--debug-output")
        if self.Debug_Trace:
            self.Args.append("--trace")
        if self.Debug_WarnUninit:
            self.Args.append("--warn-uninitialized")
        if self.Debug_WarnUnusedVars:
            self.Args.append("--warn-unused-vars")
        if self.Debug_NoWarnUnusedCli:
            self.Args.append("--no-warn-unused-cli")
        if self.CheckSystemVars:
            self.Args.append("--check-system-vars")

        # Source directory always needs to come last
        if self.SourceDirectory is not None: 
            self.Args.append(self.SourceDirectory)

        return self.Args


