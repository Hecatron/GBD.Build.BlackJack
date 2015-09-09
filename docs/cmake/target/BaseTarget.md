# BaseTarget Class

## Overview

This class represents the base class for all target related class's
A target is cmake's definitin for something to be built (similar to a Visual Studio Project)

## Properties

### Name

The name property represents the name of the target to be built

### Srcs

The Srcs property is a list of associated sources and header files to be used as part of the target

## Methods

### contructor(name: str, srcs: [] = None)

The default constructor takes several parameters

 * The name of the target to be built (any spaces will be replaced with underscores)
 * The list of sources to be associated with the target (cpp / .h files for example, this is also optional)
