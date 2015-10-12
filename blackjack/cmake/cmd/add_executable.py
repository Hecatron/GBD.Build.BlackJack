from blackjack.cmake.ScriptBase import ScriptBase
from blackjack.cmake.storage.SetList import SetList
from .cmake_set import cmake_set

class add_executable(ScriptBase):

    """
    CMake Command - Add Executable Target
    """

    def __init__(self, name: str, opts: str, srcs: []):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the target"""
        self.Options = opts
        """Executable options"""
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
        tmpline = "add_executable(" + self.Name
        if self.Options:
            tmpline += " " + self.Options
        ret.append(tmpline)
        for item in self.Srcs:
            if isinstance(item, str):
                ret.append('    "' + item + '" ')
            if isinstance(item, SetList):
                ret.append('    ' + item.Name)
        ret[-1] += ")"
        return ret
