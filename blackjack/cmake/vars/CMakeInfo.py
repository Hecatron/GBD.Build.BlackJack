from .types.CMakeVariable import CMakeVariable
from .types.VariableCollection import VariableCollection

class CMakeInfo(VariableCollection):
    """CMake Information related variables"""

    CMAKE_ARGC = ()
    CMAKE_ARGV0 = ()
    CMAKE_AR = ()
    CMAKE_BINARY_DIR = ()
    CMAKE_BUILD_TOOL = ()
    CMAKE_CACHEFILE_DIR = ()
    CMAKE_CACHE_MAJOR_VERSION = ()
    CMAKE_CACHE_MINOR_VERSION = ()
    CMAKE_CACHE_PATCH_VERSION = ()
    CMAKE_CFG_INTDIR = ()
    CMAKE_COMMAND = ()
    CMAKE_CROSSCOMPILING = ()
    CMAKE_CROSSCOMPILING_EMULATOR = ()
    CMAKE_CTEST_COMMAND = ()
    CMAKE_CURRENT_BINARY_DIR = ()
    CMAKE_CURRENT_LIST_DIR = ()
    CMAKE_CURRENT_LIST_FILE = ()
    CMAKE_CURRENT_LIST_LINE = ()
    CMAKE_CURRENT_SOURCE_DIR = ()
    CMAKE_DL_LIBS = ()
    CMAKE_EDIT_COMMAND = ()
    CMAKE_EXECUTABLE_SUFFIX = ()
    CMAKE_EXTRA_GENERATOR = ()
    CMAKE_EXTRA_SHARED_LIBRARY_SUFFIXES = ()
    CMAKE_FIND_PACKAGE_NAME = ()
    CMAKE_GENERATOR = ()
    CMAKE_GENERATOR_PLATFORM = ()
    CMAKE_GENERATOR_TOOLSET = ()
    CMAKE_HOME_DIRECTORY = ()
    CMAKE_IMPORT_LIBRARY_PREFIX = ()
    CMAKE_IMPORT_LIBRARY_SUFFIX = ()
    CMAKE_JOB_POOL_COMPILE = ()
    CMAKE_JOB_POOL_LINK = ()
    CMAKE_LINK_LIBRARY_SUFFIX = ()
    CMAKE_MAJOR_VERSION = ()
    CMAKE_MAKE_PROGRAM = ()
    CMAKE_MATCH_COUNT = ()
    CMAKE_MINIMUM_REQUIRED_VERSION = ()
    CMAKE_MINOR_VERSION = ()
    CMAKE_PARENT_LIST_FILE = ()
    CMAKE_PATCH_VERSION = ()
    CMAKE_PROJECT_NAME = ()
    CMAKE_RANLIB = ()
    CMAKE_ROOT = ()
    CMAKE_SCRIPT_MODE_FILE = ()
    CMAKE_SHARED_LIBRARY_PREFIX = ()
    CMAKE_SHARED_LIBRARY_SUFFIX = ()
    CMAKE_SHARED_MODULE_PREFIX = ()
    CMAKE_SHARED_MODULE_SUFFIX = ()
    CMAKE_SIZEOF_VOID_P = ()
    CMAKE_SKIP_INSTALL_RULES = ()
    CMAKE_SKIP_RPATH = ()
    CMAKE_SOURCE_DIR = ()
    CMAKE_STANDARD_LIBRARIES = ()
    CMAKE_STATIC_LIBRARY_PREFIX = ()
    CMAKE_STATIC_LIBRARY_SUFFIX = ()
    CMAKE_TOOLCHAIN_FILE = ()
    CMAKE_TWEAK_VERSION = ()
    CMAKE_VERBOSE_MAKEFILE = ()
    CMAKE_VERSION = ()
    CMAKE_VS_DEVENV_COMMAND = ()
    CMAKE_VS_INTEL_Fortran_PROJECT_VERSION = ()
    CMAKE_VS_MSBUILD_COMMAND = ()
    CMAKE_VS_MSDEV_COMMAND = ()
    CMAKE_VS_NsightTegra_VERSION = ()
    CMAKE_VS_PLATFORM_NAME = ()
    CMAKE_VS_PLATFORM_TOOLSET = ()
    CMAKE_XCODE_PLATFORM_TOOLSET = ()
    PROJECT_BINARY_DIR = ()
    PROJECT_NAME = ()
    PROJECT_SOURCE_DIR = ()
    PROJECT_VERSION = ()
    PROJECT_VERSION_MAJOR = ()
    PROJECT_VERSION_MINOR = ()
    PROJECT_VERSION_PATCH = ()
    PROJECT_VERSION_TWEAK = ()

    @staticmethod
    def PROJECTNAME_BINARY_DIR(projname: str):
        return CMakeVariable(projname + "_BINARY_DIR", projname)

    @staticmethod
    def PROJECTNAME_SOURCE_DIR(projname: str):
        return CMakeVariable(projname + "_SOURCE_DIR", projname)

    @staticmethod
    def PROJECTNAME_VERSION(projname: str):
        return CMakeVariable(projname + "_VERSION", projname)

    @staticmethod
    def PROJECTNAME_VERSION_MAJOR(projname: str):
        return CMakeVariable(projname + "_VERSION_MAJOR", projname)

    @staticmethod
    def PROJECTNAME_VERSION_MINOR(projname: str):
        return CMakeVariable(projname + "_VERSION_MINOR", projname)

    @staticmethod
    def PROJECTNAME_VERSION_PATCH(projname: str):
        return CMakeVariable(projname + "_VERSION_PATCH", projname)

    @staticmethod
    def PROJECTNAME_VERSION_TWEAK(projname: str):
        return CMakeVariable(projname + "_VERSION_TWEAK", projname)
