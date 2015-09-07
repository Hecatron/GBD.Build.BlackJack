# API Overview

## Overview


At the high level the class's to be most aware of are:

 * ScriptBase Class - Acts as a base class for all other script elements, allows for exporting / importing
 * Solution Class - Acts as a top level CMakeLists.txt file / Project
 * 

## Namespace List

This a general overview of the code layout within the subdirectories:

 * **blackjack.cmake** - High level wrapper classes such as Solution and SourceList
 * **blackjack.target** - High level target classes such as exe and lib targets
 * **blackjack.cmake.macros** - Usefull custom macros for inserting into scripts
 * **blackjack.cmake.cmd** - List of all standard cmake commands, low level
 * **blackjack.cmake.cmdpart** - Common groupings of parameters passed to commands
 * **blackjack.cmake.process** - Codes related to launching a cmake process

