# BlackJack Build System

## Overview

What is BlackJack?, it's simply put a python front end for cmake.
In that it generates CMakeLists.txt files via a python library code.

The best way to think of it is a form of macro expansion but using python Class's
The idea is not to try and replace cmake, since cmake is a scripting language in it's own right this would be far too complex a thing to do.
Instead we try to work along side the build process to try and automate as much of the process as possible via python.
Adding a degree of object orientation to some of the concepts such as Script files, projects, targets etc to make these easier to generate via python is the main goal.

  * [API Documentation](docs/API Overview.md)

## Why do this?

Other build systems I looked into included

 * premake - seems to be behind cmake from a popularity and functionality point of view also uses lua, also ideally I wanted a scripting language that's more debuggable
 * waf - doesn't seem to have caught on popularity wise the same as cmake.
 * meson - looks promising but still early days
 * qibuild - seems to add functionality to cmake via python for multiple repo's / some handy cmake scripts, but you still need to write CMakeLists.txt files.

Cmake seems to have the most activity in terms of development and useage, so the idea is to use the functionality that's already there but to add a layer of python frosting on top.
One of the main goals of this project is to be able to have an Object Orientated based build script, that's also debuggable.
So I figured why not have a python library that generates CMakeLists.txt files, a sort of meta-meta project build system.

Python seems to be cross platform enough that it's a reasonable language for writing cross platform build scripts in.
It's main benifits include cross platform compatibility, the fact it's easly debuggable, and that there is quite a lot of libraries written for it already.
