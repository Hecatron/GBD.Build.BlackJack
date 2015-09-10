# LibTarget_Imported Class

## Overview

Represents a CMake Imported Library target
An Imported Library Target references a lib file located outside the project.
No rules are generated to build it

## Properties

### Name

The name property represents the name of the target to be imported from the outside

### LibType

The LibType property represents the type of library to be built <br />
available values are SHARED, STATIC, MODULE, UNKNOWN from the LibTypes Enum

### GlobalImport

If to set the Global property within cmake for this target

## Methods

### contructor(name: str, libtype: LibTypes = LibTypes.UNKNOWN, globalimport: bool = False)

The default constructor takes several parameters

 * The name of the target to be built (any spaces will be replaced with underscores)
 * sets the type of library
 * If to set the GlobalImport property
