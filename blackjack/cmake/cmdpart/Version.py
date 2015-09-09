from blackjack.cmake.ScriptBase import ScriptBase

class Version(ScriptBase):

    """
    Represents a CMake style version associated with a Project
    """

    def __init__(self, major = None, minor = None, patch = None, tweak = None):
        super().__init__()
        self.Major = major
        """Major Version Number"""
        self.Minor = minor
        """Minor Version Number"""
        self.Patch = patch
        """Patch Version Number"""
        self.Tweak = tweak
        """Tweak Version Number"""
        self.AddFatalError = False
        """If to add [FATAL_ERROR] to prevent building on cmake versions lower than 2.6"""
        return

    def version_number(self):
        ret = ""
        if self.Major is not None:
            if not isinstance(self.Major, int): raise ValueError("Major Number must be an integer")
            ret += str(self.Major)
        if self.Minor is not None:
            if not isinstance(self.Minor, int): raise ValueError("Minor Number must be an integer")
            ret += "." + str(self.Minor)
        if self.Patch is not None:
            if not isinstance(self.Patch, int): raise ValueError("Patch Number must be an integer")
            ret += "." + str(self.Patch)
        if self.Tweak is not None:
            if not isinstance(self.Tweak, int): raise ValueError("Tweak Number must be an integer")
            ret += "." + str(self.Tweak)
        if self.AddFatalError == True:
            ret += " [FATAL_ERROR]"
        return ret

    def render(self):
        ret = ["VERSION " + self.version_number()]
        return ret
