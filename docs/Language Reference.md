
## Overview

## Overall Structure

* http://www.aosabook.org/en/cmake.html
* http://www.cmake.org/Wiki/CMake/Language_Syntax
* http://www.cmake.org/cmake/help/v3.2/#reference-manuals
* http://www.cmake.org/cmake/help/v3.2/manual/cmake-commands.7.html



* Each file CMakeLists.txt is a list file

## Language Ref

* comments start with # for the whole line

* CMake splits arguments unless you use quotation marks or escapes.

* The names of commands are case insensitive; the usual convention is to type the command names in uppercase.
However, the arguments are case sensitive. Thus MESSAGE and message and Message and mESsAgE are the same command

Commands are procedure calls and cannot return values. However,
you may pass the name of a global variable to some commands,
and those commands will store the result there. For example, the MATH( EXPR ... ) 
command takes three arguments; the third argument is the expression, and the second argument 
is the variable to store the result: 


MATH( EXPR x "3 + 3" ) # stores the result of 3 + 3 in x
MESSAGE( "x is ${x}" ) # displays "x is 6"
                       # using quotes so MESSAGE receives only one argument


* Variables always contain strings. Sometimes, we use the string to store a boolean,
a path to a file, an integer, or a list. 

* Almost all variables have global scope
exceptions include functions and for each loops

## Command Ref

* MESSAGE
Print to standard out

* SET / UNSET
Set or unset a variable

* MATH
perform a mathmatical calculation

* IF / ENDIF
if and endif blocks for logic




* Check the minimum version of cmake installed
    cmake_minimum_required(VERSION 2.8 FATAL_ERROR)


