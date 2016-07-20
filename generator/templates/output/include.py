from blackjack.cmake.ScriptBase import ScriptBase

class include(ScriptBase):
    """
    CMake Command - include
    """

    def __init__(self, filepath: str , optional: bool = False, resultvar: str = None, nopolicyscope: str = False):
        super().__init__()
        self.FilePath = filepath
        """File path to import, or the name of the cmake module to import"""
        self.Optional = optional
        """If Optional is set, then no error is raised if the file does not exist."""
        self.ResultVar = resultvar
        self.NoPolicyScope = nopolicyscope
		return

    @property
    def CommandName(self):
        """Name of the command"""
        return "include"

    def render_body(self):
        ret = []
        filepath = self.FilePath
        if isinstance(filepath, BaseModule):
            filepath = filepath.get_modulename()
        tmpline = "include(" + filepath + " "
        if self.Optional:
            tmpline += "OPTIONAL "
        if self.ResultVar:
            tmpline += "RESULT_VARIABLE " + self.ResultVar
        if self.NoPolicyScope:
            tmpline += "NO_POLICY_SCOPE "
        tmpline += ")"
        ret = [tmpline]
        return ret
