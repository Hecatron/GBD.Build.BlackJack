from .types.CMakeVariable import CMakeVariable
from .types.VariableCollection import VariableCollection

class CMakeLangs(VariableCollection):
    """CMake Language related variables"""

    CMAKE_C_COMPILE_FEATURES = ()
    CMAKE_C_EXTENSIONS = ()
    CMAKE_C_STANDARD = ()
    CMAKE_C_STANDARD_REQUIRED = ()
    CMAKE_CXX_COMPILE_FEATURES = ()
    CMAKE_CXX_EXTENSIONS = ()
    CMAKE_CXX_STANDARD = ()
    CMAKE_CXX_STANDARD_REQUIRED = ()
    CMAKE_Fortran_MODDIR_DEFAULT = ()
    CMAKE_Fortran_MODDIR_FLAG = ()
    CMAKE_Fortran_MODOUT_FLAG = ()
    CMAKE_INTERNAL_PLATFORM_ABI = ()

    @staticmethod
    def CMAKE_COMPILER_IS_GNU(lang: str):
        return CMakeVariable("CMAKE_COMPILER_IS_GNU" + lang, lang)

    @staticmethod
    def CMAKE_LANG_ARCHIVE_APPEND(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_ARCHIVE_APPEND", lang)

    @staticmethod
    def CMAKE_LANG_ARCHIVE_CREATE(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_ARCHIVE_CREATE", lang)

    @staticmethod
    def CMAKE_LANG_ARCHIVE_FINISH(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_ARCHIVE_FINISH", lang)

    @staticmethod
    def CMAKE_LANG_COMPILE_OBJECT(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_COMPILE_OBJECT", lang)

    @staticmethod
    def CMAKE_LANG_COMPILER_ABI(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_COMPILER_ABI", lang)

    @staticmethod
    def CMAKE_LANG_COMPILER_ID(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_COMPILER_ID", lang)

    @staticmethod
    def CMAKE_LANG_COMPILER_LOADED(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_COMPILER_LOADED", lang)

    @staticmethod
    def CMAKE_LANG_COMPILER(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_COMPILER", lang)

    @staticmethod
    def CMAKE_LANG_COMPILER_EXTERNAL_TOOLCHAIN(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_COMPILER_EXTERNAL_TOOLCHAIN", lang)

    @staticmethod
    def CMAKE_LANG_COMPILER_TARGET(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_COMPILER_TARGET", lang)

    @staticmethod
    def CMAKE_LANG_COMPILER_VERSION(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_COMPILER_VERSION", lang)

    @staticmethod
    def CMAKE_LANG_CREATE_SHARED_LIBRARY(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_CREATE_SHARED_LIBRARY", lang)

    @staticmethod
    def CMAKE_LANG_CREATE_SHARED_MODULE(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_CREATE_SHARED_MODULE", lang)

    @staticmethod
    def CMAKE_LANG_CREATE_STATIC_LIBRARY(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_CREATE_STATIC_LIBRARY", lang)

    @staticmethod
    def CMAKE_LANG_FLAGS_DEBUG(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_FLAGS_DEBUG", lang)

    @staticmethod
    def CMAKE_LANG_FLAGS_MINSIZEREL(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_FLAGS_MINSIZEREL", lang)

    @staticmethod
    def CMAKE_LANG_FLAGS_RELEASE(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_FLAGS_RELEASE", lang)

    @staticmethod
    def CMAKE_LANG_FLAGS_RELWITHDEBINFO(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_FLAGS_RELWITHDEBINFO", lang)

    @staticmethod
    def CMAKE_LANG_FLAGS(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_FLAGS", lang)

    @staticmethod
    def CMAKE_LANG_GHS_KERNEL_FLAGS_DEBUG(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_GHS_KERNEL_FLAGS_DEBUG", lang)

    @staticmethod
    def CMAKE_LANG_GHS_KERNEL_FLAGS_MINSIZEREL(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_GHS_KERNEL_FLAGS_MINSIZEREL", lang)

    @staticmethod
    def CMAKE_LANG_GHS_KERNEL_FLAGS_RELEASE(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_GHS_KERNEL_FLAGS_RELEASE", lang)

    @staticmethod
    def CMAKE_LANG_GHS_KERNEL_FLAGS_RELWITHDEBINFO(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_GHS_KERNEL_FLAGS_RELWITHDEBINFO", lang)

    @staticmethod
    def CMAKE_LANG_IGNORE_EXTENSIONS(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_IGNORE_EXTENSIONS", lang)

    @staticmethod
    def CMAKE_LANG_IMPLICIT_INCLUDE_DIRECTORIES(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_IMPLICIT_INCLUDE_DIRECTORIES", lang)

    @staticmethod
    def CMAKE_LANG_IMPLICIT_LINK_DIRECTORIES(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_IMPLICIT_LINK_DIRECTORIES", lang)

    @staticmethod
    def CMAKE_LANG_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES", lang)

    @staticmethod
    def CMAKE_LANG_IMPLICIT_LINK_LIBRARIES(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_IMPLICIT_LINK_LIBRARIES", lang)

    @staticmethod
    def CMAKE_LANG_LIBRARY_ARCHITECTURE(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_LIBRARY_ARCHITECTURE", lang)

    @staticmethod
    def CMAKE_LANG_LINKER_PREFERENCE_PROPAGATES(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_LINKER_PREFERENCE_PROPAGATES", lang)

    @staticmethod
    def CMAKE_LANG_LINKER_PREFERENCE(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_LINKER_PREFERENCE", lang)

    @staticmethod
    def CMAKE_LANG_LINK_EXECUTABLE(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_LINK_EXECUTABLE", lang)

    @staticmethod
    def CMAKE_LANG_OUTPUT_EXTENSION(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_OUTPUT_EXTENSION", lang)

    @staticmethod
    def CMAKE_LANG_PLATFORM_ID(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_PLATFORM_ID", lang)

    @staticmethod
    def CMAKE_LANG_SIMULATE_ID(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_SIMULATE_ID", lang)

    @staticmethod
    def CMAKE_LANG_SIMULATE_VERSION(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_SIMULATE_VERSION", lang)

    @staticmethod
    def CMAKE_LANG_SIZEOF_DATA_PTR(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_SIZEOF_DATA_PTR", lang)

    @staticmethod
    def CMAKE_LANG_SOURCE_FILE_EXTENSIONS(lang: str):
        return CMakeVariable("CMAKE_" + lang + "_SOURCE_FILE_EXTENSIONS", lang)

    @staticmethod
    def CMAKE_USER_MAKE_RULES_OVERRIDE_LANG(lang: str):
        return CMakeVariable("CMAKE_USER_MAKE_RULES_OVERRIDE_" + lang, lang)
