# EnvVar Class

## Overview

The EnvVar class allows for the setting of enviroment variables within cmake using the set command

## Properties

### Name

The name property represents the name of the enviroment variable that will be set

### Srcs

The Srcs property is a list of values that will be joined together and set within the variable

## Methods

### Constructor(name: str, srcs: [])

The default constructor takes several parameters

 * The name of the variable to be set.
 * The list of sources (or items to be added to the variable)

### add(items)

The add method can be used to add

 * A single item as a string
 * A list of items via a list

### add_spacesep(items_str)

The add_spacesep method can be used to add multiple items via a space seperated string
