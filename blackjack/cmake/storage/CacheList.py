from blackjack.cmake.ScriptBase import ScriptBase
from .CacheTypes import CacheTypes

class CacheList(ScriptBase):

    """
    Represents a collection of cache entries to be set
    """

    def __init__(self, name: str, srcs: [] = None, cachetype: CacheTypes = CacheTypes.STRING, docstring: str = None, force: bool = False):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the Cache Variable"""
        self.Srcs = srcs
        """List of values to set"""
        self.CacheType = cachetype
        """Type of Cache Entry"""
        self.DocString = docstring
        """Associated DocString"""
        self.Force = force
        if self.Srcs is None: self.Srcs = []
        return

    @property
    def Name(self):
        """Name of the Set"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")
        return

    def render_body(self):
        from blackjack.cmake.cmd.cmake_set import cmake_set
        ret = ["## Cachelist Set"]
        opts = "CACHE " + self.CacheType.name + " "
        opts += '"' + self.DocString + '" '
        if self.Force == True:
            opts += "FORCE"
        setcmd = cmake_set(self.Name, self.Srcs, opts)
        ret += setcmd.render()
        return ret

    def add(self, items):
        """Add a single item or list of items"""
        if isinstance(items, str):
            self.Srcs.append(items)
        if isinstance(items, list):
            self.Srcs += items
        return

    def add_spacesep(self, items_str):
        """Add a Space seperated list of items"""
        tmparr = [str(i) for i in items_str.split()]
        self.Srcs += tmparr
        return
