from cmake.ScriptBase import ScriptBase

class BaseTarget(ScriptBase):
    """Base Class for all CMake target types"""

    def __init__(self, name: str):
        super().__init__()
        self._Name = None
        self.Name = name
        """Name of the Target"""
        self.Srcs = None
        """List of Sources to include into the Target"""
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
