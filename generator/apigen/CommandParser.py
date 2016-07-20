"""
A Command parser to parse over each jinja template for a given cmake command
"""

import os
from apigen.Logger import Logger
from jinja2 import Environment, PackageLoader, FileSystemLoader

class CommandParser(object):

    def __init__(self, cmdfile: str, env: Environment, outdir: str):
        super().__init__()
        self.__log = Logger.getlogger()
        self.CommandFilePath = cmdfile
        self.__env = env
        self.OutputDirectory = outdir

    def ParseFile(self):
        cmd_basefilename = os.path.basename(self.CommandFilePath)
        self.__log.info("Parsing File: " + cmd_basefilename)
        cmd_name = os.path.splitext(cmd_basefilename)[0]
        cmd_outfile = os.path.join(self.OutputDirectory, cmd_basefilename)
 
        #if (cmd_basefilename != "add_executable.py"):
        #    return


        # Render the command output from the template
        template = self.__env.get_template(cmd_basefilename)
        tmpl_output = template.render(CmdName=cmd_name)

        # Save the File
        with open(cmd_outfile, "w") as text_file:
            text_file.write(tmpl_output)
        return
