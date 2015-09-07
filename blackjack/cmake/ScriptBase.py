import os, sys
from blackjack.logs.Logger import Logger

class ScriptBase(object):

    """
    Represents a base class for all script sections
    That can be rendered or outputted to a CMakeLists.txt file

    Within CMake there is only ever one command per line
    so each line in the text file can be thought of as a single command
    """

    def __init__(self):

        # Property Definitions
        self.__log = Logger.getlogger()
        """Class Logger"""
        self.Header = []
        """List of lines or other ScriptBase to prefix this section"""
        self.Footer = []
        """List of lines or other ScriptBase to suffix this section"""
        maindir = os.path.realpath(sys.argv[0])
        if not os.path.isdir(maindir): maindir = os.path.dirname(maindir)
        self.OutputFilePath = os.path.join(maindir, "CMakeLists.txt")
        """Default file path for exports and appends"""

    def render_body(self):
        """Virtual Method used to render the body of the Script Section"""
        return []

    def render(self):
        """
        Full render of the section including the body, footer and header
        each item within the string array is a seperate line / cmake command
        """
        # Merge together all lists
        fulllist = self.Header.copy()
        fulllist.append(self)
        fulllist += self.Footer

        # Change any ScriptBase into string arrays
        self.__log.debug("Compiling Render List")
        ret = []
        for item in fulllist:
            if isinstance(item, str):
                ret.append(item)
            if isinstance(item, ScriptBase):
                if item == self:
                    ret += item.render_body()
                else:
                    ret += item.render()
        return ret

    def render_string(self, val: [] = None):
        """Full render of the section as a single string"""
        # Get the Full array of strings
        ret= ""
        if val is not None:
            fulllist = val
        else:
            fulllist = self.render()
        if len(fulllist) == 1:
            ret = fulllist[0]
        else:
            for item in fulllist:
                ret += item + "\r\n"
        return ret

    def append(self, filepath = None):
        """Append the section as text to the given file path"""
        if filepath is None: filepath = self.OutputFilePath
        tmppath = os.path.abspath(filepath)
        txt = self.render_string()
        self.__log.debug("Appending Section to: " + tmppath)
        with open(tmppath, "a+b") as f:
            f.write(bytes(txt, 'UTF-8'))
        return

    def export(self, filepath = None):
        """Export / Overwrite the section as text to the given file path"""
        if filepath is None: filepath = self.OutputFilePath
        tmppath = os.path.abspath(filepath)
        txt = self.render_string()
        self.__log.debug("Exporting Section to: " + tmppath)
        with open(tmppath, "w+b") as f:
            f.write(bytes(txt, 'UTF-8'))
        return
 