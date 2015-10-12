from blackjack.cmake.ScriptBase import ScriptBase
from .CacheTypes import CacheTypes
from .CacheEntry import CacheEntry

class CacheList(ScriptBase):

    """
    Represents a collection of cache entries to be set
    """

    def __init__(self, cacheval: CacheEntry, force: bool = False):
        super().__init__()
        self.CacheValue = cacheval
        self.Force = force
        return

    def render_body(self):
        from blackjack.cmake.cmd.cmake_set import cmake_set
        ret = ["## Cachelist Set"]
        opts = "CACHE " + self.CacheValue.CacheType.name + " "
        opts += '"' + self.CacheValue.DocString + '" '
        if self.Force:
            opts += "FORCE"
        setcmd = cmake_set(self.CacheValue.Name, self.CacheValue.Srcs, opts)
        ret += setcmd.render()
        return ret

    def add(self, items):
        """Add a single item or list of items"""
        if isinstance(items, str):
            self.CacheValue.Srcs.append(items)
        if isinstance(items, list):
            self.CacheValue.Srcs += items
        return

    def add_spacesep(self, items_str):
        """Add a Space seperated list of items"""
        tmparr = [str(i) for i in items_str.split()]
        self.CacheValue.Srcs += tmparr
        return
