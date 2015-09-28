from .types.CMakeVariable import CMakeVariable
from .types.VariableCollection import VariableCollection

class CMakeBuildControl(VariableCollection):
    """CMake Build Control related variables"""

    CMAKE_ANDROID_API = ()
    CMAKE_ANDROID_API_MIN = ()
    CMAKE_ANDROID_GUI = ()
    CMAKE_ARCHIVE_OUTPUT_DIRECTORY = ()
    CMAKE_AUTOMOC_MOC_OPTIONS = ()
    CMAKE_AUTOMOC = ()
    CMAKE_AUTORCC = ()
    CMAKE_AUTORCC_OPTIONS = ()
    CMAKE_AUTOUIC = ()
    CMAKE_AUTOUIC_OPTIONS = ()
    CMAKE_BUILD_WITH_INSTALL_RPATH = ()
    CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY = ()
    CMAKE_DEBUG_POSTFIX = ()
    CMAKE_EXE_LINKER_FLAGS = ()
    CMAKE_Fortran_FORMAT = ()
    CMAKE_Fortran_MODULE_DIRECTORY = ()
    CMAKE_GNUtoMS = ()
    CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE = ()
    CMAKE_INCLUDE_CURRENT_DIR = ()
    CMAKE_INSTALL_NAME_DIR = ()
    CMAKE_INSTALL_RPATH = ()
    CMAKE_INSTALL_RPATH_USE_LINK_PATH = ()
    CMAKE_LIBRARY_OUTPUT_DIRECTORY = ()
    CMAKE_LIBRARY_PATH_FLAG = ()
    CMAKE_LINK_DEF_FILE_FLAG = ()
    CMAKE_LINK_DEPENDS_NO_SHARED = ()
    CMAKE_LINK_INTERFACE_LIBRARIES = ()
    CMAKE_LINK_LIBRARY_FILE_FLAG = ()
    CMAKE_LINK_LIBRARY_FLAG = ()
    CMAKE_MACOSX_BUNDLE = ()
    CMAKE_MACOSX_RPATH = ()
    CMAKE_MODULE_LINKER_FLAGS = ()
    CMAKE_NO_BUILTIN_CHRPATH = ()
    CMAKE_NO_SYSTEM_FROM_IMPORTED = ()
    CMAKE_OSX_ARCHITECTURES = ()
    CMAKE_OSX_DEPLOYMENT_TARGET = ()
    CMAKE_OSX_SYSROOT = ()
    CMAKE_PDB_OUTPUT_DIRECTORY = ()
    CMAKE_POSITION_INDEPENDENT_CODE = ()
    CMAKE_RUNTIME_OUTPUT_DIRECTORY = ()
    CMAKE_SHARED_LINKER_FLAGS = ()
    CMAKE_SKIP_BUILD_RPATH = ()
    CMAKE_SKIP_INSTALL_RPATH = ()
    CMAKE_STATIC_LINKER_FLAGS = ()
    CMAKE_TRY_COMPILE_CONFIGURATION = ()
    CMAKE_USE_RELATIVE_PATHS = ()
    CMAKE_VISIBILITY_INLINES_HIDDEN = ()
    CMAKE_VS_INCLUDE_INSTALL_TO_DEFAULT_BUILD = ()
    CMAKE_WIN32_EXECUTABLE = ()
    EXECUTABLE_OUTPUT_PATH = ()
    LIBRARY_OUTPUT_PATH = ()

    @staticmethod
    def CMAKE_ARCHIVE_OUTPUT_DIRECTORY_CONFIG(config: str):
        return CMakeVariable("CMAKE_ARCHIVE_OUTPUT_DIRECTORY_" + config, config)

    @staticmethod
    def CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY_CONFIG(config: str):
        return CMakeVariable("CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY_" + config, config)

    @staticmethod
    def CMAKE_EXE_LINKER_FLAGS_CONFIG(config: str):
        return CMakeVariable("CMAKE_EXE_LINKER_FLAGS_" + config, config)

    @staticmethod
    def CMAKE_MAP_IMPORTED_CONFIG_CONFIG(config: str):
        return CMakeVariable("CMAKE_MAP_IMPORTED_CONFIG_" + config, config)

    @staticmethod
    def CMAKE_MODULE_LINKER_FLAGS_CONFIG(config: str):
        return CMakeVariable("CMAKE_MODULE_LINKER_FLAGS_" + config, config)

    @staticmethod
    def CMAKE_PDB_OUTPUT_DIRECTORY_CONFIG(config: str):
        return CMakeVariable("CMAKE_PDB_OUTPUT_DIRECTORY_" + config, config)

    @staticmethod
    def CMAKE_LIBRARY_OUTPUT_DIRECTORY_CONFIG(config: str):
        return CMakeVariable("CMAKE_LIBRARY_OUTPUT_DIRECTORY_" + config, config)

    @staticmethod
    def CMAKE_CONFIG_POSTFIX(config: str):
        return CMakeVariable("CMAKE_" + config + "_POSTFIX", config)

    @staticmethod
    def CMAKE_LANG_INCLUDE_WHAT_YOU_USE(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_INCLUDE_WHAT_YOU_USE", lang)

    @staticmethod
    def CMAKE_LANG_VISIBILITY_PRESET(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_VISIBILITY_PRESET", lang)

    @staticmethod
    def CMAKE_RUNTIME_OUTPUT_DIRECTORY_CONFIG(config: str):
        return CMakeVariable("CMAKE_RUNTIME_OUTPUT_DIRECTORY_" + config, config)

    @staticmethod
    def CMAKE_SHARED_LINKER_FLAGS_CONFIG(config: str):
        return CMakeVariable("CMAKE_SHARED_LINKER_FLAGS_" + config, config)

    @staticmethod
    def CMAKE_STATIC_LINKER_FLAGS_CONFIG(config: str):
        return CMakeVariable("CMAKE_STATIC_LINKER_FLAGS_" + config, config)

    @staticmethod
    def CMAKE_XCODE_ATTRIBUTE_ATTR(attr: str):
        return CMakeVariable("CMAKE_XCODE_ATTRIBUTE_" + attr, attr)
