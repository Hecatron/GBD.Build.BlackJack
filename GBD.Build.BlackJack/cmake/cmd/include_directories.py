from cmake.ScriptBase import ScriptBase
import cmake.cmdpart as cmdpart

class include_directories(ScriptBase):

    """
    CMake Command - Minimum required version of CMake
    """

    def __init__(self, incdirs: [] = None):
        super().__init__()
        self.IncDirs = incdirs
        """Include Directories to add in"""
        self.Before = None
        """
        If Before = True then the includes will be prepended instead of appended
        If Before = False then the includes will be appended the same as the default
        If Before = None then the default value will be used
        """
        self.System = False
        """If the include directories are meant as System level includes"""
        return

    def render_body(self):
        ret = []
        topline = "include_directories( "
        if self.Before == True:
            topline += "BEFORE "
        if self.Before == False:
            topline += "AFTER "
        if self.System == True:
            topline += "SYSTEM "
        ret.append(topline)

        for item in self.IncDirs:
            ret.append('    "' + item + '"')
        ret.append(")")
        return ret
