# ExeTarget Class

## Overview

This class represents the standard target for an executable

## Properties

### Name

The name property represents the name of the target to be built

### Srcs

The Srcs property is a list of associated sources and header files to be used as part of the target

### Win32

If set to True Win32 will cause WIN32_EXECUTABLE to be set on the target executable

### MacosxBundle

If set to True MacosxBundle will cause MACOSX_BUNDLE to be set on the target executable

### ExludeFromAll

If set to True this will exclude the target from being built as a result of "make all"

## Methods

### contructor(name: str, srcs: [], iswin32: bool = False, macosx_bundle: bool = False , excludefromall: bool = False)

The default constructor takes several parameters

 * The name of the target to be built (any spaces will be replaced with underscores)
 * The list of sources to be associated with the target (cpp / .h files for example, this is also optional)
 * sets the Win32 property (default = False)
 * sets the MacosxBundle property (default = False)
 * sets the ExludeFromAll property (default = False)
