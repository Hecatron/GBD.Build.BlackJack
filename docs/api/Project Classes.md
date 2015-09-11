# Solution Class

## Overview

The Solution class is the top level class for CMakeLists.txt scripts <br/>
For those more familiar with Visual Studio Setups typically

 * CMake Project = Visual Studio Solution = Collection of things to build
 * CMake Target = Visual Studio Project = thing to build

In this case I've just labled the top level class a Solution
and any things to build inside a Target to try and avoid confusion.

Typically there should only be one of these class's per CMakeLists.txt file
The class inherits from the ScriptBase class which means .export() can be called to generate
the CMakeLists.txt file right next to the calling python script

The properties for this class include:

 * **Name** - The name of the cmake Project
 * **Version** - The Version of the cmake Project
 * **Langs** - Comma seperated list of supported languages for cmake, the default is "C, CXX"
 * **Min_CMakeVersion** - This is the minimum supported version of cmake required to build
   the default will be 2.8
 * **IncDirs** - This is a list of directories to use for includes globally (for all targets)
   Each item can be a seperate directory, or an instance of a IncludeDir Class (see cmdpart namespace).
   The IncludeDir class takes several different options but only some will be used for global definitions
   of include directories
 * **SourceLists** - TODO
 * **Targets** - TODO

The functions for this class include:

TODO