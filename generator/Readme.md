# Readme

## Generator

The generator represents the first stage of generating the wrapper class's needed for cmake commands.
At the time of writing cmake doesn't currently have any availabe meta-data we can use to extract commands / arguments from.
But what we need is a wrapper class for each cmake command in python that we can use to construct cmake scripts.

The current way around this is the use of a manually edited json file called **cmake_cmd_meta.json**
This file is read in via cmd_generate.py and is used to generate the initial python code stubs needed for each cmake command.

## Templates

The templates directory contains a series of Jinja2 templates used to construct the python code wrapper needed for each cmake command.
In most cases the **templates/default.py** file is used to generate the wrapper class for each command.
But it's possible to override this with custom templates (such as the one for the include directories)

## Json File

The json file is key to generating the python class's that wrap the cmake functions

  * The json file consists of a series of command declarations
  * A unique command name - 'CmdName': 'add_library'
  * If to ignore processing of the command section (defaults to false) - 'ignore': 'true'
  * Which template to use (defaults to default_tmpl.py) - 'template': 'add_custom_command_tmpl.py'
    Template inheritance can be used as all templates are jinja2 based

  * Within the Command there is a jinja section, this acts as a text replacement block for replacing
    blocks of text such as lists of arguments, or the python code needed to render the command.
  * A list of arguments for the constructor of the wrapper class is provided within the args section
    Each one of these arguments is stored within the class as a similar named property
    The json definition is Name, Type, Description, Default Value


  * TODO try adding comments with double slashes
    see https://github.com/vaidik/commentjson/blob/master/commentjson/commentjson.py

{'Commands': [

  {					// Decleration of a Command
    'CmdName': 'add_library',		// The unique command name
    'Jinja': {				// This is the start of the jinja replacement block
      'args': 'name: str, opts: str, srcs: []',
      'render': 'ret = "{{ CmdName }}(" + self.name + ")"'
    }
  },

  {						// Decleration of a Command
    'CmdName': 'add_executable',		// The unique command name
    'ignore': 'false',				// If to ignore processing of this command - defaults to false
    'template': 'add_custom_command_tmpl.py',	// Use a template other than the default one
    'Jinja': {					// This is the start of the jinja replacement block
      'args': [					// List of arguments to take as input
        {'Name', 'str', 'Name of the target'},
        {'Options', 'str', 'Executable options'},
        {'Srcs', '[]', 'List of Sources to include into the target'},
        ],
    }
  },

] }