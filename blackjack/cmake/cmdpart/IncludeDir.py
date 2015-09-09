from blackjack.cmake.ScriptBase import ScriptBase
from .ScopeTypes import ScopeTypes

class IncludeDir(ScriptBase):

    """
    Represents a CMake style include directory
    """

    def __init__(self, dirnames: [], scopetype: ScopeTypes = ScopeTypes.PUBLIC, system: bool = False, before: bool = None):
        super().__init__()
        self.DirNames = dirnames
        """Directory Names"""
        self.ScopeType = scopetype
        """Scope of Definition"""
        self.System = system
        self.Before = before
        return

    def render(self):
        """Default is used for Targets"""
        ret = []
        tmpline = ""
        if self.System == True:
            tmpline += "SYSTEM "
        if self.Before == True:
            tmpline += "BEFORE "
        tmpline += self.ScopeType.name
        ret.append(tmpline)
        for item in self.DirNames:
            ret.append('    "' + item + '"')
        return ret

    def render_global(self):
        """This one is used for global include directories"""
        ret = []
        tmpline = ""
        if self.Before == True:
            tmpline += "BEFORE "
        if self.Before == False:
            tmpline += "AFTER "
        if self.System == True:
            tmpline += "SYSTEM "
        if tmpline:
            tmpline = "    " + tmpline
        ret.append(tmpline)
        for item in self.DirNames:
            ret.append('    "' + item + '"')
        return ret
