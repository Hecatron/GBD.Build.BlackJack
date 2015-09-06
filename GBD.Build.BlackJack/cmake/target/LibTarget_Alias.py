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
        self._Target = None
        self.Target = target
        """Destination Target to link to"""
        return

    @property
    def Target(self):
        """Name of the Target"""
        return self._Target

    @Target.setter
    def Target(self, value):
        self._Target = value.replace(" ", "_")
        return

    def render_body(self):
        ret = ["## Library Target - Alias"]
        libcmd = cmd.add_library(self.Name, "ALIAS " + self.Target, [])
        ret += libcmd.render()
        return ret
