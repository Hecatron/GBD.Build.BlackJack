# IncludeDir Class

## Overview

This class can be used for creating more advanced versions of include directories
to be inputted into a Target or Solution.

## Properties

### DirNames

This is simply just a list of relative or absolute directory names for inclusion

### ScopeType

The scope type only applies for use within targets, it defines the scope of the include directory
via the enum ScopeTypes

### System

If set to true will include the SYSTEM flag within the include directory definition

### Before

This can be set to one of 3 different values

 * None (default) - no qualifier specified
 * True - the "BEFORE" qualifier is specified
 * False - the "AFTER" qualifier is specified

## Methods

### render()

This function renders an output for use with the Target Class's or target_include_directories

### render_global()

This function renders an output for use with the Solution Class's or include_directories
