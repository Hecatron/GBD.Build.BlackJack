# LibType_Alias Class

## Overview

This class represents an alias target for a library.
In that an alias can be used as a way of referencing the original target via a different name

## Properties

### Name

The name property represents the name of the target to be built

### Target

The Target property references the target that this alias needs to point to

## Methods

### contructor(name: str, target: str)

The default constructor takes several parameters

 * The name of the target to be built (any spaces will be replaced with underscores)
 * The destination target that this one points / relates to
