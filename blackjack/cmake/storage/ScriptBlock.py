from blackjack.cmake.ScriptBase import ScriptBase
import os

class ScriptBlock(ScriptBase):

    """
    Represents a specific block of text
    Imported from a file, or text string with newlines
    """

    def __init__(self, contents: [] = None):
        super().__init__()
        self.Contents = contents
        if self.Contents == None:
            self.Contents = []
        return

    def render_body(self):
        """Virtual Method used to render the body of the Script Section"""
        return self.Contents

    def importstring(self, val: str):
        """Import a string block seperated by new lines into the class storage"""
        self.Contents = val.splitlines()
        return self.Contents

    def importfile(self, filepath: str):
        """Import the given file into the class storage"""
        tmppath = os.path.abspath(filepath)
        if os.path.exists(tmppath) == False:
            raise FileNotFoundError("File for import not found: " + tmppath)
        instr = ""
        with open(tmppath, "r") as f:
            instr = f.read()
        self.importstring(instr)
        return instr
