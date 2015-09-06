import cmake.cmd as cmd
from .BaseTarget import BaseTarget

class LibTarget_Object(BaseTarget):

    """
    Represents a CMake Object Library target
    An object library compiles source files but does not archive or link their object files into a library.

    add_library(<name> OBJECT <src>...)
    """

    def __init__(self, name: str, srcs: []):
        super().__init__(name)
        self.Srcs = srcs
        """List of Sources to include into the Target"""
        return

    def render_body(self):
        ret = ["## Library Target - Object"]
        libcmd = cmd.add_library(self.Name, "OBJECT", self.Srcs)
        ret += libcmd.render()
        return ret
