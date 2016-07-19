"""
Represents the meta data for cmake function definitions in json
"""

import json
from pprint import pprint

class CMakeMeta(object):

    MetaFilePath = "cmake_cmd_meta.json"

    def ParseFile(self):
        with open(MetaFilePath) as data_file:    
            data = json.load(data_file)
        pprint(data)
