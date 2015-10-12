import blackjack.cmake.cmd as cmd
from .BaseTarget import BaseTarget

class LibTarget_Interface(BaseTarget):

    """
    Represents a CMake Interface Library target
    An Interface library target does not directly create build output
    though it may have properties set on it and it may be installed, exported and imported

    add_library(<name> INTERFACE [IMPORTED [GLOBAL]])
    """

    def __init__(self, name: str, imported: bool = False, globalimport: bool = False):
        super().__init__(name)
        self.Imported = imported
        """If the library is imported"""
        self.GlobalImport = globalimport
        """Global Import"""
        return

    def render_body(self):
        ret = []
        ret += ["## Library Target - Interface"]
        ret += super().render_prefix()
        tmpopts = "INTERFACE"
        if self.Imported:
            tmpopts += " IMPORTED"
            if self.GlobalImport:
                tmpopts += " GLOBAL"

        libcmd = cmd.add_library(self.Name, tmpopts, [])
        ret += libcmd.render()
        ret += super().render_body()
        return ret
