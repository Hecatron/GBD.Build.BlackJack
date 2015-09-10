import blackjack.cmake.cmd as cmd
from .BaseTarget import BaseTarget

class ExeTarget_Alias(BaseTarget):

    """
    Represents a CMake Alias Executable target
    An Alias Executable Target is just a shortcut / alias to another existing exe target

    add_executable(<name> ALIAS <target>)
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
        ret = []
        ret += ["## Executable Target - Alias"]
        ret += super().render_prefix()
        execmd = cmd.add_executable(self.Name, "ALIAS " + self.Target, [])
        ret += execmd.render()
        ret += super().render_body()
        return ret
