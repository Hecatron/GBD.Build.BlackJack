from blackjack.cmake.ScriptBase import ScriptBase

class EnvVar(ScriptBase):

    """
    Represents the setting of an Enviromnent Variable
    """

    def __init__(self, name: str, srcs: []):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the enviroment variable to set"""
        self.Srcs = srcs
        """List of values for the variable"""
        return

    @property
    def Name(self):
        """Name of the enviroment variable to set"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")
        return

    def render_body(self):
        from blackjack.cmake.cmd.cmake_set import cmake_set
        ret = ["## EnvVar Set"]
        setcmd = cmake_set("ENV{" + self.Name + "}", self.Srcs)
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
