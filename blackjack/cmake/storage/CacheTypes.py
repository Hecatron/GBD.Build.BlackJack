from enum import Enum

class CacheTypes(Enum):
    """Type of Cache Entry to create Enum"""
    BOOL = 1
    FILEPATH = 2
    PATH = 3
    STRING = 4
    INTERNAL = 5
