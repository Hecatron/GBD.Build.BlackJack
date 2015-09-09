from blackjack.cmake.ScriptBase import ScriptBase
from blackjack.cmake.cmdpart.Version import Version

class project(ScriptBase):

    """
    CMake Command - Project Defintion
    """

    def __init__(self, name: str, version: Version = None, langs: str = None):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the project"""
        self.Version = version
        """Version associated with the project"""
        self.Langs = langs
        """Languages associated with the project"""

        # Set Defaults
        if self.Version is None: self.Version = Version(0,0)
        if self.Langs is None: self.Langs = "C, CXX"
        return

    @property
    def Name(self):
        """Name of the list / set"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")

    def render_body(self):
        ret = []
        tmpline = "project(" + self.Name + " "
        if self.Version:
            tmpline += self.Version.render_string() + " "
        if self.Langs:
            tmpline += "LANGUAGES " + self.Langs
        tmpline += ")"
        ret.append(tmpline)
        return ret

