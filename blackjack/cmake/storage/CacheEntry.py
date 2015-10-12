from blackjack.cmake.ScriptBase import ScriptBase
from .CacheTypes import CacheTypes

class CacheEntry(object):
    """Representation of a cmake cache entry"""

    def __init__(self, name: str, srcs: [] = None, cachetype: CacheTypes = CacheTypes.STRING, docstring: str = None):
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
        if self.Srcs is None: self.Srcs = []
        return

    @property
    def Name(self):
        """Name of the Cache Entry"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")
        return

    def render_body(self):
        ret = []
        ret.append("//" + self.DocString)
        cmdval = ""
        for item in self.Srcs:
            cmdval += item + ";"
        cmdval = cmdval[:-1]
        cmd = self._Name + ":" + self.CacheType + "=" + cmdval
        ret.append(cmd)
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
