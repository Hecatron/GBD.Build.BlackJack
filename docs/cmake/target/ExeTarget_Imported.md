# ExeTarget_Imported Class

## Overview

Represents a CMake Imported Executable target
An Imported Executable Target references a exe file located outside the project.
No rules are generated to build it

## Properties

### Name

The name property represents the name of the target to be imported from the outside

### GlobalImport

If to set the Global property within cmake for this target

## Methods

### contructor(name: str, globalimport: bool = False)

The default constructor takes several parameters

 * The name of the target to be built (any spaces will be replaced with underscores)
 * If to set the GlobalImport property
