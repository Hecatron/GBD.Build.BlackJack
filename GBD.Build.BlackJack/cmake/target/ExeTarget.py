from .BaseTarget import BaseTarget

class ExeTarget(BaseTarget):
    
    """
    Represents a CMake Executable target
    """

    def __init__(self, name: str):
        super().__init__(name)
        return

    # TODO add_executable

    def render_body(self):
        ret = ["## Exe Target"]

        #setcmd = cmd.cmake_set("CompilerFlags", self.Vars)
        #ret += setcmd.render()

        #ret += cmd.foreach("CompilerFlag", [setcmd]).render()
        #for replaceitem in self.Replacements:
        #    replacestr = '  string(REPLACE '
        #    replacestr += '"' + replaceitem[0] + '" '
        #    replacestr += '"' + replaceitem[1] + '" '
        #    replacestr += '${CompilerFlag} "${${CompilerFlag}}")'
        #    ret.append(replacestr)
        #ret += cmd.endforeach().render()
        return ret