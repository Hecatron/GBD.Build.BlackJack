from blackjack.cmake.ScriptBase import ScriptBase

class cmake_set(ScriptBase):

    """
    CMake Command - Set / List of items
    """

    def __init__(self, name: str, srcs: [], opts: str = None):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the Set"""
        self.Srcs = srcs
        """List of Sources"""
        self.Options = opts
        """Options to pass to set"""
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
        if self.Options:
            ret.append(self.Options)
        ret[-1] += ")"
        return ret
