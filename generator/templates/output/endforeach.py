from blackjack.cmake.ScriptBase import ScriptBase

class endforeach(ScriptBase):
    """
    CMake Command - endforeach
    """

    def __init__(self, loopvar: str ):
        super().__init__()
        self.LoopVar = loopvar
        """Loop Variable to end the foreach loop with"""
		return

    @property
    def CommandName(self):
        """Name of the command"""
        return "endforeach"

    def render_body(self):
        ret = []
        ret = ["endforeach(" + self.LoopVar + ")"]
        return ret
