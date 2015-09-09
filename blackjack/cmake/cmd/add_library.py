from blackjack.cmake.ScriptBase import ScriptBase
from blackjack.cmake.storage.SourceList import SourceList
from .cmake_set import cmake_set

class add_library(ScriptBase):

    """
    CMake Command - Add Library Target
    """

    def __init__(self, name: str, opts: str, srcs: []):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the target"""
        self.Options = opts
        """Type of library to use, and library options"""
        self.Srcs = srcs
        """List of Sources to include into the target"""
        return

    @property
    def Name(self):
        """Name of the target"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")

    def render_body(self):
        ret = []
        tmpline = "add_library(" + self.Name
        if self.Options:
            tmpline += " " + self.Options
        ret.append(tmpline)
        for item in self.Srcs:
            if isinstance(item, str):
                ret.append('    "' + item + '" ')
            if isinstance(item, SourceList):
                ret.append('    ' + item.Name)
        ret.append(")")
        return ret
