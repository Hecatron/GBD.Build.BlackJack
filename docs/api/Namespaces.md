# Namespaces

## blackjack.cmake

This namespace is the top level, it includes Solution and ScriptBase classes.

 * **ScriptBase** - Is the class that all other script elements inherit from
 * **Solution** - This represents a single CMakeLists.txt file / cmake Project.

## blackjack.cmake.cmd

The cmd namespace contains all the low level cmake commands represented as python classes.
Normally these shouldn't need to be called for the most part if using the higher level class's.

Since the script blocks (ScriptBase) are just arrays of strings (each item is one line),
it's possible to append any text you want at any stage and just bypass these classes altogether.

## blackjack.cmake.cmdpart

The cmdpart namespace contains several helper classes that represent blocks of text to be passed to a cmake command.

 * **Version** - Takes several integers as parameters for the version number, then renders a string that can be used for cmake_minimum_required or project
 * **IncludeDir** - Can be used as an input to the Solution or Target Include directories property

## blackjack.cmake.modules

Modules contains helper classes for rendering blocks of cmake script, kind of similar to a macro.

 * **FlagsReplace** - Class for generating a block of cmake code for replacing flags within a set of variables
 * **FlagsReplaceCompiler** - Similar to the FlagsReplace class but just auto specified all the variables used for C Compilers

## blackjack.cmake.modules.cmake

The modules.cmake namespace contains wrappers for some of the modules included with cmake.
All of these classes should inherit from the BaseModule class.
Note with these modules we need to make sure we do an **include** statement before using the module.

## blackjack.cmake.process

The process namespace contains anything related to actually launching cmake after the CMakeLists.txt file
has been generated.

## blackjack.cmake.storage

The storage namespace contains wrapper classes assocaited with storage of variables within cmake.

 * **ScriptBlock** - includes functions for importing text files from the outside and is basically an externally imported file.
 * **SetList** - represents a set variable within cmake which basically an array of strings each one typically beinga path to a source file
 * **EnvVar** - represents the setting of an Enviromental Variable.
 * **CacheList** - uses cmake's set command to set Cache variables within the cmake cache.

## blackjack.cmake.target

The target namespace contains all classes related to cmake targets

 * **BaseTarget** - Base class for all targets to inherit from

 * **ExeTarget** - Basic Executable target
 * **ExeTarget_Alias** - Executable target which is actually a shortcut (similar to a symbolic link) to another executable target.
 * **ExeTarget_Imported** - Executable target which has been imported from outside of the build system.

 * **LibTypes** - Enum listing all the availble cmake library types
 * **LibTarget** - Standard library target
 * **LibTarget_Alias** - Library target which is actually a shortcut (similar to a symbolic link) to another library target.
 * **LibTarget_Imported** - Library target which has been imported from outside of the build system.
 * **LibTarget_Interface** - Interface type library target.
 * **LibTarget_Object** - Target used for compiling sources into an object, which can then be later linked into another target.

## blackjack.cmake.util

The util namespace contains classes that don't seem to fall into any one catagory.
This could include "message", or "include" for example.

## blackjack.cmake.vars

The vars namespace contains references to all the cmake inbuilt variables.
Most of these are defines as enums and can be referenced by name

 * **CompilerID** - List of all available compiler id's within cmake