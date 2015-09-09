# Version Class

## Overview

This class is just a shortcut to producing a cmake compatible version string.
It's possible to use this as a part of the Solution class for the Project version
or to specify the minimum version of cmake required.

## Properties

### Major

Major Version number

### Minor

Minor Version number

### Patch

Patch Version number

### Tweak

Tweak Version number

### AddFatalError

This is a boolean, if true adds "FATAL_ERROR" to the end of the version number
this prevents cmake versions 2.4 and lower from running the script
