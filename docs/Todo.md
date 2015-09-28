# TODO

## General

1. Look into running the cmake process via pexpect / winpexpect

2. add a property to Solution called ToolchainScript which if set adds a definition to load in the toolchain file

3. Add a function to CMakeVariable base class to read off the value from cmake
   during python runtime

4. Look into comments feeding into doxygen
and redo docs for the main high level classes to use, remove cmake subdir, add to api subdir

## Visual Studio

1. Read in Visual Studio Project xml files and change to a Target Class
Ideally we want it to look at NMake based projects first
namespace of blackjack.vstudio

## CMake Commands

### Existig Classes

#### Solution Class

 * add_compile_options(<option> ...)
 * add_custom_command
 * add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
 * enable_testing()
 * link_libraries([item1 [item2 [...]]] [[debug|optimized|general] <item>] ...)
 * enable_language
 * link_directories
 * include_regular_expression

#### BaseTarget Class

 * target_compile_options(<target> [BEFORE] <INTERFACE|PUBLIC|PRIVATE> [items1...] [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
 * target_compile_features(<target> <PRIVATE|PUBLIC|INTERFACE> <feature> [...])
 * target_link_libraries
 * set_target_properties(target1 target2 ... PROPERTIES prop1 value1 prop2 value2 ...)
 * add_dependencies(<target> [<target-dependency>]...)

##### AddSources Target Class

 * target_sources(<target> <INTERFACE|PUBLIC|PRIVATE> [items1...] [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

##### Custom Target Class

 * add_custom_target

##### External MS Project Target Class

 * include_external_msproject

#### Definitions Class - New, used within Project and BaseTarget

 * add_definitions(-DFOO -DBAR ...)
 * remove_definitions
 * target_compile_definitions(<target> <INTERFACE|PUBLIC|PRIVATE> [items1...] [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

#### SourceList Class

 * aux_source_directory(<dir> <variable>)
 * unset

### Test Classes

 * add_test(NAME <name> COMMAND <command> [<arg>...] [CONFIGURATIONS <config>...] [WORKING_DIRECTORY <dir>])
 * set_tests_properties
 * create_test_sourcelist

### Process Classes

 * execute_process
 * build_command

### Properties Classes

we need a whole new family of class's for properties <br />
http://www.cmake.org/cmake/help/v3.3/manual/cmake-properties.7.html

 * get_property
 * set_property
 * define_property
 * get_cmake_property
 * get_target_property
 * get_test_property
 * get_source_file_property
 * get_directory_property
 * set_directory_properties
 * set_source_files_properties

Class's include:

 * Global
 * Directories
 * Targets
 * Tests
 * Source Files
 * Cache Entries
 * Installed Files

### Util Classes

 * message
 * file
 * export
 * cmake_host_system_information
 * configure_file
 * get_filename_component
 * fltk_wrap_ui
 * include
 * option
 * qt_wrap_cpp
 * qt_wrap_ui
 * site_name
 * variable_watch

### Cache Related

 * load_cache
 * mark_as_advanced

### Storage related

 * separate_arguments
 * source_group

### Policies Classes

 * cmake_policy

### Find Classes

 * find_file
 * find_library
 * find_package
 * find_path
 * find_program

### Install Classes

 * install

### Logic - cmd only

 * if
 * elseif
 * else
 * endif
 * endwhile
 * break
 * function
 * macro
 * while
 * endmacro
 * endfunction
 * string
 * math
 * return
 * continue
 * try_compile
 * try_run
 * list
