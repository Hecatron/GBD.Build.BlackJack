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

        # Remove globbing expressions from the cmake cache
        for item in self.GlobbingRemoveExpr:
            self.Args.append("-U" + str(item))

        # Add the Generator if specified
        if self.Generator is not None: 
            self.Args.append("-G" + str(self.Generator))

        # Specify Toolset name
        if self.ToolsetName is not None:
            self.Args.append("-T" + str(self.ToolsetName))

        # Specify Platform name
        if self.PlatformName is not None:
            self.Args.append("-A" + str(self.PlatformName))

        # Suppress Developer Warnings
        if self.SuppressDevelWarns == True:
            self.Args.append("-Wno-dev")

        # Enable Developer Warnings
        if self.EnableDevelWarns == True:
            self.Args.append("-Wdev")

        # View only mode
        if self.ViewMode == True:
            self.Args.append("-N")

        # Specify Process Script mode
        if self.ProcessScriptMode is not None:
            self.Args.append("-P" + str(self.ProcessScriptMode))



        # TODO Add additional options
        # --debug-trycompile
        # --debug-output
        # --trace
        # --warn-uninitialized
        # --warn-unused-vars
        # --no-warn-unused-cli
        # --check-system-vars



        # Source directory always needs to come last
        if self.SourceDirectory is not None: 
            self.Args.append(self.SourceDirectory)

        return self.Args


    # TODO
    # -E <command>
    # -L[A][H] List non-advanced cached variables.

    # --find-package
    # --graphviz=[file]
    # --system-information [file]
