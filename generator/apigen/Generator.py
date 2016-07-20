"""
A Generator to generate the lower level API bindings for scripting cmake commands
"""

import os
from apigen.Logger import Logger
from apigen.CommandParser import CommandParser
from jinja2 import Environment, FileSystemLoader

class Generator(object):

    def __init__(self):
        super().__init__()
        self.__log = Logger.getlogger()
        self.__jinjaenv = None
        self.Base_TemplateDir = 'templates/base/'
        self.Command_TemplateDir = 'templates/cmds/'
        self.Command_OutputDir = 'templates/output/'
        
    def Generate(self):

        # Setup Jinja Templating Environment
        tmpl_dirs = [self.Base_TemplateDir, self.Command_TemplateDir]
        self.__jinjaenv = Environment(loader=FileSystemLoader(tmpl_dirs))

        self.__log.info("Generating Command API's via Jinja")
        for file in os.listdir(self.Command_TemplateDir):
            if file.endswith(".py"):
                filepath = os.path.abspath(os.path.join(self.Command_TemplateDir, file))
                cmdparser = CommandParser(filepath, self.__jinjaenv, self.Command_OutputDir)
                cmdparser.ParseFile()
