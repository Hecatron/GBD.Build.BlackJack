import blackjack.cmake.cmd as cmd
from .BaseTarget import BaseTarget
from .LibTypes import LibTypes

class LibTarget_Imported(BaseTarget):

    """
    Represents a CMake Imported Library target
    An Imported Library Target references a library file located outside the project. No rules are generated to build it

    add_library(<name> <SHARED|STATIC|MODULE|UNKNOWN> IMPORTED [GLOBAL])
    """

    def __init__(self, name: str, libtype: LibTypes = LibTypes.UNKNOWN, globalimport: bool = False):
        super().__init__(name)
        self._LibType = None
        self.LibType = libtype
        """Library Type"""
        self.GlobalImport = globalimport
        """Global Import"""
        return

    @property
    def LibType(self):
        """Library Type"""
        return self._LibType

    @LibType.setter
    def LibType(self, value):
        if value != LibTypes.SHARED and value != LibTypes.STATIC and value != LibTypes.MODULE and value != LibTypes.UNKNOWN:
            raise ValueError("Invalid value for Library Type")
        self._LibType = value

    def render_body(self):
        ret = ["## Library Target - Imported"]
        tmpopts = self.LibType.name + " IMPORTED"
        if self.GlobalImport == True:
            tmpopts += " GLOBAL"
        libcmd = cmd.add_library(self.Name, tmpopts, [])
        ret += libcmd.render()
        return ret
