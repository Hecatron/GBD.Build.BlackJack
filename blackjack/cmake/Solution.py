
import os
from .ScriptBase import ScriptBase
from blackjack.cmake.cmdpart.Version import Version

class Solution(ScriptBase):

    """
    Represents a single CMake Project
    Note there can only be one Project per CMakeLists.txt file
    This class represents the top level for a given script file
    """

    def __init__(self, name: str, version: Version = None, langs: str = None, cmakemin: Version = None):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the project"""
        self.Version = version
        """Version associated with the project"""
        self.Langs = langs
        """Languages associated with the project"""
        self.Min_CMakeVersion = cmakemin
        """Minimum version of cmake required"""
        self.IncDirs = []
        """Global Include Directories"""
        self.SourceLists = []
        """List of Sets to add to the Project"""
        self.Targets = []
        """List of Targets to add to the Project"""

        # Set Defaults
        if self.Version is None: self.Version = Version(0,0)
        if self.Langs is None: self.Langs = "C, CXX"
        if self.Min_CMakeVersion is None: self.Min_CMakeVersion = Version(2,8)
        return

    @property
    def Name(self):
        """Name of the list / set"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")


    def render_body(self):
        import blackjack.cmake.cmd as cmd

        """Render the Project Body of the script"""
        if self.Name is None: raise ValueError("Project Name cannot be empty")
        if not isinstance(self.Name, str): raise ValueError("Project Name must be a string")
        if not isinstance(self.Version, Version): raise ValueError("Project Version must be a Version class")
        if not isinstance(self.Langs, str): raise ValueError("Project Langs must be a string")
        if not isinstance(self.Min_CMakeVersion, Version): raise ValueError("Project CMake Minimum Version must be a Version class")

        ret = ["## BlackJack Project Defintion"]
        # Add the Minimum required version for cmake
        cmd1 = cmd.cmake_minimum_required(self.Min_CMakeVersion)
        ret += cmd1.render()

        # Add the Project Defintion
        cmd2 = cmd.project(self.Name, self.Version, self.Langs)
        ret += cmd2.render()

        # Add in Global Include Directories
        cmd3 = cmd.include_directories(self.IncDirs)
        ret += cmd3.render()

        # Add the Set Lists
        for item in self.SourceLists:
            ret += item.render()

        # Add the list of Targets
        for item in self.Targets:
            ret += item.render()

        return ret
