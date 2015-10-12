from blackjack.cmake.ScriptBase import ScriptBase
from blackjack.cmake.cmd.target_include_directories import target_include_directories

# TODO Include Directories

class BaseTarget(ScriptBase):
    """Base Class for all CMake target types"""

    def __init__(self, name: str, srcs: [] = None):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the Target"""
        self.Srcs = srcs
        """List of Sources to include into the Target"""
        self.IncDirs = []
        """Target Include Directories"""
        self.SetLists = []
        """List of Sets to add to the Target"""
        return

    @property
    def Name(self):
        """Name of the Target"""
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value.replace(" ", "_")
        return

    def get_objname(self):
        """Returns the target name in a Object Form for inclusion into other targets"""
        ret = "$<TARGET_OBJECTS:" + self.Name + ">"
        return ret

    def get_fullsrcs(self):
        """This function returns the full list of sources and the list of set names"""
        setnames = []
        for item in self.SetLists:
            setnames.append(item.Name)
        setnames += self.Srcs
        return setnames

    def render_prefix(self):
        # Add the Set Lists
        ret = []
        for item in self.SetLists:
            ret += item.render()
        return ret

    def render_body(self):
        ret = []
        # Add in Target Include Directories
        cmd1 = target_include_directories(self.Name, self.IncDirs)
        ret += cmd1.render()
        return ret
