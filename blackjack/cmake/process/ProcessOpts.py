import sys

class ProcessOpts(object):
    """Represents command line options passed to a cmake process"""

    def __init__(self, cmakepath:str = None):

        self.ExeSuffix = ""
        if sys.platform == 'win32': self.ExeSuffix = ".exe"
        # Assume cmake is in the current path
        self.CMakeBinPath = "cmake" + self.ExeSuffix
        """Binary path to the cmake executable"""
        if cmakepath is not None: self.CMakePath = cmakepath

        self.SourceDirectory = None
        """Directory where the CMakeLists.txt files will be sourced"""

        self.BuildDirectory = None
        """Directory where the output from running cmake will be placed"""

        self.LogFile = sys.stdout
        """Log destination when running cmake"""

        self.Generator = None
        """Which generator to use when creating the make build files"""

    def get_opts(self):
        """Get command line options"""
        # The Build directory is used as the working directory when running cmake
        ret = list()

        # TODO Add additional options
        if self.Generator is not None: ret.append('-G' + str(self.Generator))

        # Source directory always needs to come last
        if self.SourceDirectory is not None: ret.append(self.SourceDirectory)
        return ret


#        self._preload_cache = None
#        self._defines = []
#        self._globbing_expr = None
#        self._generator_name = None
#        self._toolset_name = None
#        self._platform_name = None
#        self._warnings_developer = False
#        self._command = None
#        self._list_vars = None
#        self._build_tree = None
#        self._viewonly = False
#        self._process_script = None
#        self._find_package = False
#        self._graphviz = None
#        self._sysinfo = None

#        #self._trace_mode = False
#        #self._help_mode = False
#        #self._warnings_uninitialized = False
#        #self._warnings_nounused_cli = False
#        return

#    # TODO Process script via stdin option

#    #version_mode = property_type("_trace_mode", bool, "CMake version mode")
#    #help_mode = property_type("_help_mode", bool, "CMake help mode")
#    #output_trace = property_type("_output_trace", bool, "CMake trace output")
#    #output_debug = property_type("_output_debug", bool, "CMake debug output")
#    #warnings_uninitialized = property_type("_warnings_uninitialized", bool, "Warn about uninitialized values")
#    #warnings_nounused_cli = property_type("warnings_nounused_cli", bool, "Don't warn about command line options.")

#    def render(self):
#        """Render the command line options we'll pass to cmake"""
#        ret = []
#        # Build directory needs to be the current working directory for cmake, so we can't add that here

#        if self._preload_cache is not None:
#            ret.append("-C" + self._preload_cache)

#        if self._defines is not None:
#            if self._defines.count > 0:
#                for item in self._defines:
#                    ret.append("-D" + item)
        
#        if self._globbing_expr is not None:
#            ret.append("-U" + self._globbing_expr)

#        if self._generator_name is not None:
#            ret.append("-G" + self._generator_name)

#        if self._toolset_name is not None:
#            ret.append("-T" + self._toolset_name)

#        if self._platform_name is not None:
#            ret.append("-A" + self._platform_name)

#        if self._warnings_developer == True:
#            ret.append("-Wdev")
#        else:
#            ret.append("-Wno-dev")
        
#        if self._command == True:
#            ret.append("-E " + self._command)

#        if self._list_vars is not None:
#            ret.append("-L" + self._list_vars)

#        if self._build_tree is not None:
#            ret.append("--build " + self._build_tree)

#        if self._viewonly == True:
#            ret.append("-N")

#        if self._process_script is not None:
#            ret.append("-P" + self._process_script)

#        if self._find_package == True:
#            ret.append("--find-package")

#        if self._graphviz is not None:
#            ret.append("--graphviz=" + self._graphviz)

#        if self._sysinfo is not None:
#            ret.append("--system-information " + self._sysinfo)

#        # Source directory should be last option if specified        
#        if self._source_directory is not None: ret.append(self._source_directory)
#        return ret
