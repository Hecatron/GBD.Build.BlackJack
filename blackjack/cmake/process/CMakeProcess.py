﻿
# TODO

# pexpect info
# https://pexpect.readthedocs.org/en/latest/overview.html

import winpexpect as pexpect

class CMakeProcess(object):
    """Represents a CMake Process that can be called externally"""

    def __init__(self):
        # Assume cmake is in the current path
        self.cmakepath = "cmake"

        #self._cmake_options = CMakeProcessOpts()

    # Class Properties
    #cmake_options = property_type("_cmake_options", str, "Options to be passed to cmake")

    # TODO Get list of generators, and get version

    def get_version(self):
        proc = pexpect.winspawn(self.cmakepath,["--version"])
        proc.logfile = sys.stdout

        #proc.

        #proc.expect('\n>')
        return

    # TODO clean CMake cache
    # TODO Run cmake to process

    # https://pexpect.readthedocs.org/en/latest/overview.html