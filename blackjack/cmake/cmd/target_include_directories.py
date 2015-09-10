from blackjack.cmake.ScriptBase import ScriptBase
from blackjack.cmake.cmdpart.IncludeDir import IncludeDir

class target_include_directories(ScriptBase):

    """
    CMake Command - Include Directories for Target
    """

    def __init__(self, name: str, incdirs: [] = None):
        super().__init__()
        self.Name = name
        """Represents the Target Name"""
        self.IncDirs = incdirs
        """Include Directories to add in"""
        return

    def render_body(self):
        # First split the array into strings, and IncludeDir class's
        ret = []
        inc_strs = []
        inc_cls = []
        for item in self.IncDirs:
            if isinstance(item, str):
                inc_strs.append(item)
            if isinstance(item, IncludeDir):
                inc_cls.append(item)

        # Include any "string only" include directories
        if len(inc_strs) > 0:
            ret.append("target_include_directories( " + self.Name)
            for item in inc_strs:
                ret.append('    PUBLIC "' + item + '"')
            ret[-1] += ")"

        # Include any directories specified via the IncludeDir class
        for item in inc_cls:
            ret.append("target_include_directories( " + self.Name)
            ret += item.render()
            ret[-1] += ")"
        return ret
