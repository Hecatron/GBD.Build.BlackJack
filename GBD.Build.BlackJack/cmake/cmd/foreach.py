from cmake.ScriptBase import ScriptBase
from cmake.SourceList import SourceList
from .cmake_set import cmake_set
import cmake.cmdpart as cmdpart

class foreach(ScriptBase):

    """
    CMake Command - ForEach Loop
    """

    def __init__(self, loopvar: str, loopitems: []):
        super().__init__()
        self.LoopVar = loopvar
        """Loop Variable to start the foreach loop with"""
        self.LoopItems = loopitems
        """Items to loop over"""
        return

    def render_body(self):
        ret = ["foreach(" + self.LoopVar + " "]
        for item in self.LoopItems:
            if isinstance(item, str):
                ret.append(item + " ")
            if isinstance(item, SourceList):
                ret.append("${" + item.Name + "} ")
        ret[-1] += ")"
        return ret
