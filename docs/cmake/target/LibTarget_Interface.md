# LibTarget_Interface Class

## Overview

Represents a CMake Interface Library target
An Interface library target does not directly create build output,
though it may have properties set on it and it may be installed, exported and imported.

## Properties

### Name

The name property represents the name of the target to be imported from the outside

### Imported

Defines if the library is imported

### GlobalImport

If to set the Global property within cmake for this target

## Methods

### contructor(name: str, imported: bool = False, globalimport: bool = False)

The default constructor takes several parameters

 * The name of the target to be built (any spaces will be replaced with underscores)
 * if the library is imported
 * If to set the GlobalImport property
