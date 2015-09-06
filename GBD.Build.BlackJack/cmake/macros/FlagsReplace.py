from cmake.ScriptBase import ScriptBase
import cmake.cmd as cmd

class FlagsReplace(ScriptBase):

    """
    Helper Class to replace Flags within specified variables
    """

    def __init__(self, vars: [], replacements: []):
        super().__init__()
        self.Vars = vars
        """Variables to loop over and replace flags within"""
        self.Replacements = replacements
        """List of Replacements to perform on the Variable contents"""
        return


    def render_body(self):
        ret = ["## Flags Replace Macro"]
        setcmd = cmd.cmake_set("CompilerFlags", self.Vars)
        ret += setcmd.render()

        ret += cmd.foreach("CompilerFlag", [setcmd]).render()
        for replaceitem in self.Replacements:
            replacestr = '  string(REPLACE '
            replacestr += '"' + replaceitem[0] + '" '
            replacestr += '"' + replaceitem[1] + '" '
            replacestr += '${CompilerFlag} "${${CompilerFlag}}")'
            ret.append(replacestr)
        ret += cmd.endforeach().render()
        return ret
