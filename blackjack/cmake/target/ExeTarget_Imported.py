import blackjack.cmake.cmd as cmd
from .BaseTarget import BaseTarget

class ExeTarget_Imported(BaseTarget):

    """
    Represents a CMake Imported Executable target
    An Imported Executable Target references a exe file located outside the project. No rules are generated to build it

    add_executable(<name> IMPORTED [GLOBAL])
    """

    def __init__(self, name: str, globalimport: bool = False):
        super().__init__(name)
        self.GlobalImport = globalimport
        """Global Import"""
        return

    def render_body(self):
        ret = []
        ret += ["## Executable Target - Imported"]
        ret += super().render_prefix()
        tmpopts = "IMPORTED "
        if self.GlobalImport == True:
            tmpopts += "GLOBAL "
        execmd = cmd.add_executable(self.Name, tmpopts, [])
        ret += execmd.render()
        ret += super().render_body()
        return ret
