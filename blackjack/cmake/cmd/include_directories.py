from blackjack.cmake.ScriptBase import ScriptBase
from blackjack.cmake.cmdpart.IncludeDir import IncludeDir

class include_directories(ScriptBase):

    """
    CMake Command - Include Directories
    """

    def __init__(self, incdirs: [] = None):
        super().__init__()
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

        # Include any string only include directories
        if len(inc_strs) > 0:
            ret.append("include_directories(")
            for item in inc_strs:
                ret.append('    "' + item + '"')
            ret.append(")")

        # Include any directories specified via the IncludeDir class
        for item in inc_cls:
            ret.append("include_directories(" + item.render_string(item.render_global()))
            ret.append(")")
        return ret
