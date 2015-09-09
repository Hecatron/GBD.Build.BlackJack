# CacheList Class

## Overview

The CacheList class allows for the setting of cache variables within cmake using the set command

## Properties

### Name

The name property represents the name of the cache variable that will be set

### Srcs

The Srcs property is a list of values that will be joined together and set within the variable

## Methods

### contructor(name: str, srcs: [] = None, cachetype: CacheTypes = CacheTypes.STRING, docstring: str = None, force: bool = False)

The default constructor takes several parameters

 * The name of the cache variable to be set.
 * The list of values to be set within that varaible
 * type of cache variable
 * docstring / description associated with that variable
 * If to force the cache variable over the top of a value already set

### add(items)

The add method can be used to add

 * A single item as a string
 * A list of items via a list

### add_spacesep(items_str)

The add_spacesep method can be used to add multiple items via a space seperated string
