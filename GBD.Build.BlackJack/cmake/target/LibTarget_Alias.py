import cmake.cmd as cmd
from .BaseTarget import BaseTarget

class LibTarget_Alias(BaseTarget):

    """
    Represents a CMake Alias Library target
    An Alias Library Target is just a shortcut / alias to another existing library target

    add_library(<name> ALIAS <target>)
    """

    def __init__(self, name: str, target: str):
        super().__init__(name)
        self.Target = target
        """Destination Target to link to"""
        return

    def render_body(self):
        ret = ["## Library Target - Alias"]
        libcmd = cmd.add_library(self.Name, "ALIAS " + self.Target, [])
        ret += libcmd.render()
        return ret
