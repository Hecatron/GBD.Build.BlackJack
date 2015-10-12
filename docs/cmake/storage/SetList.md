# SetList Class

## Overview

SetList is basically a set within cmake, it's the setting of a variable in the context
of setting a list of sources for a given target

## Properties

### Name

The Name property defines the name of the set variable that will be created within cmake.
These tend to have a global scope, so it's best to be aware of name clashes when defining these.
Also any spaces within the name will be auto replaced with underscores

### Srcs

The Srcs property is a list of values that will be set within the cmake variable.
Typically it's a list of source files, or relative paths to source files to be included into a target.

### ParentScope

If to also set the variable within the parent scope

## Methods

### constructor(name: str, srcs: [] = None, parentscope: bool = False)

The default constructor takes several parameters

 * The name of the variable to be set.
 * The list of sources (or items to be added to the variable)
 * The parentscope field will default to False / not specified if not provided

### add(items)

The add method can be used to add

 * A single item as a string
 * A list of items via a list
 * All the items from another SetList class

### add_spacesep(items_str)

The add_spacesep method can be used to add multiple items via a space seperated string
