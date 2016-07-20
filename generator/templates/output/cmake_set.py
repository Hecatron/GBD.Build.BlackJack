from blackjack.cmake.ScriptBase import ScriptBase

class cmake_set(ScriptBase):
    """
    CMake Command - cmake_set
    """

    def __init__(self, name: str , sources: [] , options: str = None):
        super().__init__()
        self.Name = name
        """Name of the target / set"""
        self.Sources = sources
        """List of Sources to include into the target / set"""
        self.Options = options
        """Options"""
		return

    @property
    def CommandName(self):
        """Name of the command"""
        return "cmake_set"

    def render_body(self):
        ret = []
        tmpline = "cmake_set(" + self.Name
        if self.Options:
            tmpline += " " + self.Options
        ret.append(tmpline)
        for item in self.Sources:
            if isinstance(item, str):
                ret.append('    "' + item + '" ')
            if isinstance(item, SetList):
                ret.append('    ' + item.Name)
        ret[-1] += ")"
        return ret
