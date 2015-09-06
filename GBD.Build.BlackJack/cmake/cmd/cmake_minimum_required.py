from cmake.ScriptBase import ScriptBase
import cmake.cmdpart as cmdpart

class cmake_minimum_required(ScriptBase):

    """
    CMake Command - Minimum required version of CMake
    """

    def __init__(self, version = None):
        super().__init__()
        self.Version = version
        """Minimum required version of cmake"""
        if self.Version is None: self.Version = cmdpart.Version(2,8)
        return

    def render_body(self):
        ret = []
        ret.append("cmake_minimum_required(" + self.Version.render() + ")")
        return ret
