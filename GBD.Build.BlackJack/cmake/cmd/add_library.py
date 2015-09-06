from cmake.ScriptBase import ScriptBase
from cmake.SourceList import SourceList
from .cmake_set import cmake_set
import cmake.cmdpart as cmdpart

class add_library(ScriptBase):

    """
    CMake Command - Add Library Target
    """

    def __init__(self, name: str, opts: str, srcs: []):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the project"""
        self.Srcs = srcs
        """List of Sources to include into the target"""
        self.Options = opts
        """Type of library to use, and library options"""
        return

    @property
    def Name(self):
        """Name of the list / set"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")

    def render_body(self):
        ret = []
        tmpline = "add_library(" + self.Name
        if self.Options is not None:
            tmpline += " " + self.Options
        ret.append(tmpline)
        for item in self.Srcs:
            if isinstance(item, str):
                ret.append('"' + item + '" ')
            if isinstance(item, SourceList):
                ret.append(item.Name)
        ret.append(")")
        return ret
