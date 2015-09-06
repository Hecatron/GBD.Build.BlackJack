#from helper.PropertyHelper import property_type

#class CMakeProcessOpts(object):
#    """Represents command line options passed to a cmake process"""

#    def __init__(self):
#        self._source_directory = None
#        self._build_directory = None
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

#    # Class Properties
#    source_directory = property_type("_source_directory", str, "Source Directory, working directory used by cmake")
#    build_directory = property_type("_build_directory", str, "Build Directory, output for build files used by cmake")
#    preload_cache = property_type("_preload_cache", str, "Pre-load a script to populate the cache")
#    defines = property_type("_defines", list, "Defines set for cmake via -D")
#    globbing_expr = property_type("_globbing_expr", str, "Remove matching entries from CMake cache")
#    generator_name = property_type("_generator_name", str, "Specify a build system generator")
#    toolset_name = property_type("_toolset_name", str, "Specify toolset name if supported by the generator")
#    platform_name = property_type("_platform_name", str, "Specify platform name if supported by the generator")
#    warnings_developer = property_type("_warnings_developer", bool, "If to enable developer warnings for CMake")
#    command = property_type("_command", str, "Set CMake for Command Mode, and run the specified command")
#    list_vars = property_type("_list_vars", str, "List variables from within the cache, pass in A or H for additional values")
#    build_tree = property_type("_build_tree", str, "Build a CMake-generated project binary tree")
#    viewonly = property_type("_viewonly", bool, "View mode only")
#    process_script = property_type("_process_script", str, "Process script mode")
#    find_package = property_type("_find_package", bool, "Run in pkg-config like mode")
#    graphviz = property_type("_graphviz", str, "Generate graphviz of dependencies, see CMakeGraphVizOptions.cmake for more")
#    sysinfo = property_type("_sysinfo", str, "Dump information about this system")

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
