from .ScriptBase import ScriptBase

class SourceList(ScriptBase):

    """
    Represents a collection of source files to be passed to a Target
    """

    def __init__(self, name: str, srcs: [] = None, parentscope: bool = False):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the Set"""
        self.Srcs = srcs
        """List of Sources"""
        self.ParentScope = parentscope
        """If to set the list within the parent scope"""
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
        from cmake.cmd.cmake_set import cmake_set
        ret = ["## Source Set"]
        libcmd = cmake_set(self.Name, self.Srcs, self.ParentScope)
        ret += libcmd.render()
        return ret

    def add(self, items):
        """Add a single item or list of items"""
        if isinstance(items, str):
            self.Srcs.append(items)
        if isinstance(items, list):
            self.Srcs += items
        if isinstance(items, SourceList):
            self.Srcs += items.Srcs
        return

    def add_spacesep(self, items_str):
        """Add a Space seperated list of items"""
        tmparr = [str(i) for i in items_str.split()]
        self.Srcs += tmparr
        return
