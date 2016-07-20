from blackjack.cmake.ScriptBase import ScriptBase

class foreach(ScriptBase):
    """
    CMake Command - foreach
    """

    def __init__(self, loopvar: str , loopitems: str ):
        super().__init__()
        self.LoopVar = loopvar
        """Loop Variable for the foreach loop"""
        self.LoopItems = loopitems
        """Items to loop over"""
		return

    @property
    def CommandName(self):
        """Name of the command"""
        return "foreach"

    def render_body(self):
        ret = []
        ret = ["foreach(" + self.LoopVar + " "]
        for item in self.LoopItems:
            if isinstance(item, str):
                ret.append(item + " ")
            if isinstance(item, SetList):
                ret.append("${" + item.Name + "} ")
        ret[-1] += ")"
        return ret
