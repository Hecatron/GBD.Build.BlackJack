from enum import Enum

class LibTypes(Enum):
    """Type of Library to create Enum"""
    DEFAULT = 1
    STATIC = 2
    SHARED = 3
    MODULE = 4
    OBJECT = 5
    UNKNOWN = 6
