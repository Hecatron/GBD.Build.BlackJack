from cmake.ScriptBase import ScriptBase
import cmake.cmdpart as cmdpart

class endforeach(ScriptBase):

    """
    CMake Command - End of ForEach Loop
    """

    def __init__(self, loopvar: str = ''):
        super().__init__()
        self.LoopVar = loopvar
        """Loop Variable to end the foreach loop with"""
        return

    def render_body(self):
        ret = ["endforeach(" + self.LoopVar + ")"]
        return ret
