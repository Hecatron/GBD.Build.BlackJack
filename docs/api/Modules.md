# Modules

## BlackJack Modules

BlackJack modules are effectivley blocks of python code to render usefull blocks
of cmake code

Typically these are located under blackjack.cmake.modules

 * **FlagsReplace** - This class is a helper class for specifying string
   replacements within given cmake variables during cmake runtime
 * **FlagsReplaceCompiler** - This class is a wrapper around FlagsReplace
   It specifies a common set of variables used for C / C++ Compiler variables
   this includes: CMAKE_CXX_FLAGS, CMAKE_CXX_FLAGS_DEBUG, 
   CMAKE_CXX_FLAGS_RELEASE, CMAKE_C_FLAGS, CMAKE_C_FLAGS_DEBUG, CMAKE_C_FLAGS_RELEASE

## CMake Modules

CMake modules are blocks of cmake code located as part of the cmake installation
Within windows you'll typically see them under C:\Program Files (x86)\CMake\share\cmake-3.3\Modules
there's also a list under http://www.cmake.org/cmake/help/v3.3/manual/cmake-modules.7.html

There are some wrapper classes for these under blackjack.cmake.modules.cmake

With CMake modules it's important to note that you have to use an include statement to
include the module name before it can be used.
