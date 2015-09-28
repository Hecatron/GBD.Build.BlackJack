from enum import Enum

class AutoEnum(Enum):
    """
    Auto Numbering Enum
    
    The value can be overriden
    if -1 is specified then the value from the prior enum definition will be used
    """

    def __new__(cls, override: int = None):
        value = len(cls.__members__)
        if override is not None:
            if override == -1:
                value = value -1
            else:
                value = override
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __str__(self):
        """Return a string of the assigned name by default"""
        return str(self.name)
