# Script Classes

## ScriptBase

The first class from which most other class's inherit is the ScriptBase Class.
This class represents a single block of script within the CMakeFile.txt generation

There are typically 3 Parts which make up the final rendered output

 * **Header** - simple list
 * **Body** - renderd via render_body()
 * **Footer** - simple list

Both the header and the footer can ether be a list of strings or other ScriptBase class's.
The Body is a virtual method that renders the main output of the class.

Generally speaking most class's render they're output via render_body, the header and footer sections
are more like optional ways for the end user to insert other commands or blocks of text before or after
a given section or specific command. Since CMake is a scripting language in it's own right I wanted to make
sure that the setup would be flexible enough to allow for inserting sections before or after any block.

The properties for this class include:

 * **Header** - A Simple list of strings, or other ScriptBase related class's that is rendered before the main body
 * **Footer** - A Simple list of strings, or other ScriptBase related class's that is rendered after the main body
 * **OutputFilePath** - The default file path for file exports, the default is to a CMakeLists.txt file within the 
   same directory as the main running script.

The functions for this class include:

 * **render_body()** - render_body is the main function to be overridden by any derived class,
   it's job is to simply return a string list with each item in the list representing a single line.
   It's worh noting that cmake typically doesn't have multiple commands on a given line.

 * **render()** - The render function is a simple wrapper around render body, it adds the header and
   footer before and after the main script body. For any other ScriptBase Class's found in the header
   or footer these are also rendered out as string lists.

 * **render_string()** - The render_string function takes the output from render() and converts the list into
   a single string with newlines added to seperate each line in the text block.

 * **append(filepath)** - Append takes the file content from render_string() then appends it to a given file path.
   If no filepath is given the default will be to write the contents to CMakeLists.txt within the same
   directory as the main script. Append will add to the bottom of any file currently existing on that path.

 * **export(filepath)** - Export takes the file content from render_string() then writes it to a given file path.
   If no filepath is given the default will be to write the contents to CMakeLists.txt within the same
   directory as the main script. Export will overwrite any file currently existing on that path.

## ScriptBlock

The ScriptBlock class is a very simple container class that is derrived from ScriptBase
It's job is just to act as a simple string list container

The idea is we can use this class to import a block of text from an external file for later import into a rendered cmake file

The properties for this class include:

 * **Body** - represents the text imported from a file or string with lines.

The functions for this class include:

 * **importstring(val)** - This will read in a string with lines, then seperate out each line into the Body array property
 * **importfile(filepath)** - This will read in a file with lines, then seperate out each line into the Body array property

Body is a simple string list that is outputed via render_body()
This can be manipulated via code to contain any strings lines required

## ToolchainFile

Normally when starting cmake, it makes an attempt to detect which compiler / linker to use.
In some cases we want to override this and force it to use a compiler we've specified.
This is usually true in cross compiling situations.
The normal way to do this is to create a seperate script file,
then get cmake to load this prior to doing anything else (such as processing CMakeLists.txt)

By defining CMAKE_TOOLCHAIN_FILE when cmake is run from the command line we can cause cmake
to process the file specified before doing anything else

The ToolchainFile is just a class inherited from ScriptBlock, the only difference
is that it overrides the default export file path to "CMakeToolChain.txt"

If we provide a ToolchainFile class to the ToolchainFile property of the Solution class
then during the launching of cmake, CMAKE_TOOLCHAIN_FILE will be set to the filepath of that class

### Links

 * http://www.cmake.org/Wiki/CMake_Cross_Compiling

TODO Example