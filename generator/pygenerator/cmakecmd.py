"""
Represents the meta data for a single cmake command read from json
"""

import json
from pprint import pprint

class CMakeCmd(object):

    def __init__(self, json: str):
        super().__init__()
        self.JSON = json
