# FlagsReplace Class

## Overview

The FlagsReplace class is a helper class for specifying string replacements within given cmake variables
during cmake runtime

THe FlagsReplaceCompiler Class is a wrapper around this one for specifying a common list of C++ flags
to replace, this includes: CMAKE_CXX_FLAGS, CMAKE_CXX_FLAGS_DEBUG, 
CMAKE_CXX_FLAGS_RELEASE, CMAKE_C_FLAGS, CMAKE_C_FLAGS_DEBUG, CMAKE_C_FLAGS_RELEASE

## Properties

### Vars

The cmake variables to initite the replacements on

### Replacements

The Replacements property is an array of paired values to replace one flag with another

## Methods

### contructor(self, vars: [], replacements: [])

The default constructor takes several parameters

 * The list of variables to initite the replacements on.
 * An array of paired values to replace one flag with another
