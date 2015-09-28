from types import DynamicClassAttribute

class CMakeVariable(object):
    """Representation of a single CMake Variable."""

    def __init__(self, name: str, param: str = None):
        super().__init__()
        self._name_ = name
        self._param_ = param
        return

    # We use DynamicClassAttribute as a way of defining a read only property

    @DynamicClassAttribute
    def name(self):
        """The name of the CMake Variable."""
        return self._name_

    @DynamicClassAttribute
    def param(self):
        """The parameter used to create the variable."""
        return self._param_

    def __str__(self):
        """Return a string of the assigned name by default"""
        return str(self._name_)
