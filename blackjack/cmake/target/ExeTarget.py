import blackjack.cmake.cmd as cmd
from .BaseTarget import BaseTarget

class ExeTarget(BaseTarget):
    
    """
    Represents a CMake Executable target

    add_executable(<name> [WIN32] [MACOSX_BUNDLE] [EXCLUDE_FROM_ALL] source1 [source2 ...])
    """

    def __init__(self, name: str, srcs: [] = [], iswin32: bool = False, macosx_bundle: bool = False , excludefromall: bool = False):
        super().__init__(name)
        self.Srcs = srcs
        """List of Sources to include into the Target"""
        self.Win32 = iswin32
        """If WIN32 is given the property WIN32_EXECUTABLE will be set on the target created"""
        self.MacosxBundle = macosx_bundle
        """If MACOSX_BUNDLE is given the property MACOSX_BUNDLE is set on the target created"""
        self.ExludeFromAll = excludefromall
        """If to exlude from the default make all"""
        return

    def render_body(self):
        ret = []
        ret += ["## Executable Target - Normal"]
        ret += super().render_prefix()
        tmpopts = ""
        if self.Win32:
            tmpopts += "WIN32 "
        if self.MacosxBundle:
            tmpopts += "MACOSX_BUNDLE "
        if self.ExludeFromAll:
            tmpopts += "EXCLUDE_FROM_ALL "
        execmd = cmd.add_executable(self.Name, tmpopts, self.get_fullsrcs())
        ret += execmd.render()
        ret += super().render_body()
        return ret
