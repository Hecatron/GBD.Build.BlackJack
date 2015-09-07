from blackjack.cmake.ScriptBase import ScriptBase

class cmake_set(ScriptBase):

    """
    CMake Command - Set / List of items
    """

    def __init__(self, name: str, srcs: [], parentscope: bool = False):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the Set"""
        self.Srcs = srcs
        """List of Sources"""
        self.ParentScope = parentscope
        """If to set the list within the parent scope"""
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
        ret = []
        ret.append("set(" + self.Name + " ")
        for item in self.Srcs:
            ret.append('    "' + item + '"')
        if self.ParentScope == True:
            ret.append("PARENT_SCOPE")
        ret.append(")")
        return ret
