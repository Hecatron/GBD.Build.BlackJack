from blackjack.cmake.ScriptBase import ScriptBase
from .cmake_set import cmake_set

class cmake_set_env(cmake_set):

    """
    CMake Command - Set Enviromental Variable
    """

    def __init__(self, name: str, listitems: [] = None):
        super().__init__(name, listitems, False)
        return

    def render_body(self):
        ret = []
        ret.append("set(ENV{" + self.Name + "} ")
        for item in self.ListItems:
            ret.append('    "' + item + '"')
        ret.append(")")
        return ret
