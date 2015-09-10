# LibTarget Class

## Overview

This class represents the standard target for a library

## Properties

### Name

The name property represents the name of the target to be built

### Srcs

The Srcs property is a list of associated sources and header files to be used as part of the target

### LibType

The LibType property represents the type of library to be built <br />
available values are STATIC, SHARED, MODULE, DEFAULT from the LibTypes Enum

The DEFAULT value results in a blank value being used for the library type so that the default value
that cmake has in mind at the time will be used for the library

### ExludeFromAll

If set to True this will exclude the target from being built as a result of "make all"

## Methods

### contructor(name: str, srcs: [], libtype: LibTypes = LibTypes.DEFAULT, excludefromall: bool = False)

The default constructor takes several parameters

 * The name of the target to be built (any spaces will be replaced with underscores)
 * The list of sources to be associated with the target (cpp / .h files for example, this is also optional)
 * sets the type of library
 * sets the ExludeFromAll property (default = False)
