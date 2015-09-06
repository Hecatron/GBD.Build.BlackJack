# BlackJack Build System

## Overview

What is BlackJack?, it's simply put a python front end for cmake.
In that it generates CMakeLists.txt files via a python library code.

The idea is not to try and replace cmake completely, since cmake is a scripting language in it's own right this would be far too complex a thing to do.
Instead we try to work along side the build process to try and automate as much of the process as possible via python.
Adding a degree of object orientation to some of the concepts such as Script files, projects, targets etc to make these easier to generate via python is the main goal.

## Why do this?

Other build systems I looked into included

 * premake - seems to be behind cmake from a popularity and functionality point of view also uses lua, ideally I want a scripting language that's more debuggable
 * waf - doesn't seem to have caught on popularity wise the same as cmake.
 * meson - looks promising but still early days
 * qibuild - seems to add functionality to cmake via python for multiple repo's / some handy cmake scripts, but you still need to write CMakeLists.txt files.

Cmake seems to have the most activity in terms of development and useage, so the idea is to use the functionality that's already there but to add a layer of python on top.
One of the main goals of this project is to be able to have an Object Orientated based build script, that's also debuggable.
So I figured why not have a python library that generates CMakeLists.txt files, a sort of meta-meta project build system.

Originally I looked into the use of CS-Script for something written via C# Scripts but that probably wouldn't be as cross platform as python.
Also it still seems like early days for CS-Script and Roslyn .csx file support.

Python seems to be cross platform enough that it's a reasonable language for writing cross platform build scripts in.
It's main benifits include cross platform compatibility, the fact it's easly debuggable, and that there is quite a lot of libraries written for it already.

## Sub Pages

  * [1.1 Project Dependencies](docs/1.1 Project Dependencies.md)
  * [1.2 Project Components](docs/1.2 Project Components.md)
  * [1.3 Example Use Cases](docs/1.3 Example Use Cases.md)

## TODO Required Modules

Make sure your using the pip from python version 3.x

For Linux:

  * pip install pexpect

For windows:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32
https://bitbucket.org/geertj/winpexpect/wiki/Home
https://pexpect.readthedocs.org/en/latest/index.html

  * C:\Python34\Scripts\pip install winpexpect
  * C:\Python34\Scripts\pip install http://www.lfd.uci.edu/~gohlke/pythonlibs/3i673h27/pywin32-219-cp34-none-win32.whl

pypiwin32