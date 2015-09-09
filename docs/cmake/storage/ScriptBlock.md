# ScriptBlock Class

## Overview

The ScriptBlock class is a very simple container class that is derrived from ScriptBase
It's job is just to act as a simple string list container

## Properties

### Body

Body is a simple string list that is outputed via render_body()
This can be manipulated via code to contain any strings lines required

## Methods

### constructor(contents: [] = None)

The constructor takes a single optional input which can be an array of text lines to store
within the body property of the class.

### importstring(val)

importstring will read in a string with new lines, then seperate out each line into the Contents array

### importfile(filepath)

importfile simply reads in a text file then parses the contents via importstring to read in the contents
into the Contents property string list
