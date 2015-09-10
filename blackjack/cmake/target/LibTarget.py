import blackjack.cmake.cmd as cmd
from .BaseTarget import BaseTarget
from .LibTypes import LibTypes

class LibTarget(BaseTarget):
    
    """
    Represents a CMake Library target

    add_library(<name> [STATIC | SHARED | MODULE] [EXCLUDE_FROM_ALL] source1 [source2 ...])
    """

    def __init__(self, name: str, srcs: [], libtype: LibTypes = LibTypes.DEFAULT, excludefromall: bool = False):
        super().__init__(name)
        self.Srcs = srcs
        """List of Sources to include into the Target"""
        self._LibType = None
        self.LibType = libtype
        """Type of Library"""
        self.ExludeFromAll = excludefromall
        """If to exlude from the default make all"""
        return

    @property
    def LibType(self):
        """Library Type"""
        return self._LibType

    @LibType.setter
    def LibType(self, value):
        if value != LibTypes.DEFAULT and value != LibTypes.STATIC and value != LibTypes.SHARED and value != LibTypes.MODULE:
            raise ValueError("Invalid value for Library Type")
        self._LibType = value

    def render_body(self):
        ret = []
        ret += ["## Library Target - Normal"]
        ret += super().render_prefix()
        tmpopts = ""
        if self.LibType != LibTypes.DEFAULT:
            tmpopts += self.LibType.name + " "
        if self.ExludeFromAll == True:
            tmpopts += "EXCLUDE_FROM_ALL "
        libcmd = cmd.add_library(self.Name, tmpopts, self.get_fullsrcs())
        ret += libcmd.render()
        ret += super().render_body()
        return ret

