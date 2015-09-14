from .BaseEnum import BaseEnum
from types import DynamicClassAttribute

class CMakeSystem(BaseEnum):
    """CMake System related variables"""

    APPLE = ()
    BORLAND = ()
    CMAKE_CL_64 = ()
    CMAKE_COMPILER_2005 = ()
    CMAKE_HOST_APPLE = ()
    CMAKE_HOST_SYSTEM_NAME = ()
    CMAKE_HOST_SYSTEM_PROCESSOR = ()
    CMAKE_HOST_SYSTEM = ()
    CMAKE_HOST_SYSTEM_VERSION = ()
    CMAKE_HOST_UNIX = ()
    CMAKE_HOST_WIN32 = ()
    CMAKE_LIBRARY_ARCHITECTURE_REGEX = ()
    CMAKE_LIBRARY_ARCHITECTURE = ()
    CMAKE_OBJECT_PATH_MAX = ()
    CMAKE_SYSTEM_NAME = ()
    CMAKE_SYSTEM_PROCESSOR = ()
    CMAKE_SYSTEM = ()
    CMAKE_SYSTEM_VERSION = ()
    CYGWIN = ()
    ENV = ()
    GHS_MULTI = ()
    MINGW = ()
    MSVC10 = ()
    MSVC11 = ()
    MSVC12 = ()
    MSVC14 = ()
    MSVC60 = ()
    MSVC70 = ()
    MSVC71 = ()
    MSVC80 = ()
    MSVC90 = ()
    MSVC_IDE = ()
    MSVC = ()
    MSVC_VERSION = ()
    UNIX = ()
    WIN32 = ()
    WINCE = ()
    WINDOWS_PHONE = ()
    WINDOWS_STORE = ()
    XCODE_VERSION = ()

    @DynamicClassAttribute
    def name(self):
        """The name of the Enum member."""
        if self._name_ == "GHS_MULTI": return "GHS-MULTI"
        return self._name_
