# TODO

## General

1. Look into comments feeding into doxygen
2. Look into running the cmake process via pexpect / winpexpect
3. Look into cmake variables via constants

## Visual Studio

1. Read in Visual Studio Project xml files and change to a Target Class
Ideally we want it to look at NMake based projects first

## Targets

1. custom target
2. target properties
3. target_link_libraries
4. add custom command

## CMake Commands

### Project Class

 * add_compile_options(<option> ...)
 * add_custom_command
 * add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
 * enable_testing()
 * link_libraries([item1 [item2 [...]]] [[debug|optimized|general] <item>] ...)
 * enable_language
 * link_directories

### New Definitions Class, used within Project and BaseTarget

 * add_definitions(-DFOO -DBAR ...)
 * remove_definitions
 * target_compile_definitions(<target> <INTERFACE|PUBLIC|PRIVATE> [items1...] [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

### Include Directories class, modify the Target class to use this one

 * target_include_directories(<target> [SYSTEM] [BEFORE] <INTERFACE|PUBLIC|PRIVATE> [items1...] [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])

### BaseTarget Class

 * target_compile_options(<target> [BEFORE] <INTERFACE|PUBLIC|PRIVATE> [items1...] [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
 * target_compile_features(<target> <PRIVATE|PUBLIC|INTERFACE> <feature> [...])
 * target_link_libraries
 * target_sources(<target> <INTERFACE|PUBLIC|PRIVATE> [items1...] [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
 * set_target_properties(target1 target2 ... PROPERTIES prop1 value1 prop2 value2 ...)
 * add_dependencies(<target> [<target-dependency>]...)
 * add_custom_target

### New Test Class

 * add_test(NAME <name> COMMAND <command> [<arg>...] [CONFIGURATIONS <config>...] [WORKING_DIRECTORY <dir>])
 * set_tests_properties

### SourceList related

 * aux_source_directory(<dir> <variable>)
 * unset

### Process related

 * execute_process
 * build_command

### Multiple uses

 * set_property
 * define_property
 * get_cmake_property
 * string

### Logic

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

### Unsorted

 * add_executable
 * add_library
 * cmake_host_system_information
 * cmake_minimum_required
 * cmake_policy
 * configure_file
 * continue
 * create_test_sourcelist
 * endforeach
 * export
 * file
 * find_file
 * find_library
 * find_package
 * find_path
 * find_program
 * fltk_wrap_ui
 * foreach
 * get_directory_property
 * get_filename_component
 * get_property
 * get_source_file_property
 * get_target_property
 * get_test_property
 * if
 * include_directories
 * include_external_msproject
 * include_regular_expression
 * include
 * install
 * list
 * load_cache
 * load_command
 * mark_as_advanced
 * math
 * message
 * option
 * project
 * qt_wrap_cpp
 * qt_wrap_ui
 * return
 * separate_arguments
 * set_directory_properties
 * set
 * set_source_files_properties
 * site_name
 * source_group
 * try_compile
 * try_run
 * variable_watch
