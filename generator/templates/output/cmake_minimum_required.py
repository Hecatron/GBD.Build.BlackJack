from blackjack.cmake.ScriptBase import ScriptBase

class cmake_minimum_required(ScriptBase):
    """
    CMake Command - cmake_minimum_required
    """

    def __init__(self, version: Version ):
        super().__init__()
        self.Version = version
        """Minimum required version of cmake"""
        if self.Version is None: self.Version = Version(2,8)
		return

    @property
    def CommandName(self):
        """Name of the command"""
        return "cmake_minimum_required"

    def render_body(self):
        ret = []
        ret.append("cmake_minimum_required(" + self.Version.render_string() + ")")
        return ret
