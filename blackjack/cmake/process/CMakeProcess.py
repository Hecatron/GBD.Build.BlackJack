
# TODO

# pexpect info
# https://pexpect.readthedocs.org/en/latest/overview.html

import blackjack.contrib.pexpect.wexpect as pexpect
#import blackjack.contrib.pexpect.pexpect as pexpect
#import wexpect as pexpect
#import pexpect as pexpect
import sys, time

class CMakeProcess(object):
    """Represents a CMake Process that can be called externally"""

    def __init__(self):
        # Assume cmake is in the current path
        self.cmakepath = "cmake.exe"

        #self._cmake_options = CMakeProcessOpts()

    # Class Properties
    #cmake_options = property_type("_cmake_options", str, "Options to be passed to cmake")

    # TODO Get list of generators, and get version

    def get_version(self):


        #proc = pexpect.spawn("ftp.exe")
        proc = pexpect.spawn(self.cmakepath,["--version"])

        # Log everything to stdout
        proc.logfile = sys.stdout

        proc.send("test")

        # Forces the output to be flushed into the before property
        proc.expect(pexpect.EOF)

        #proc.logfile = sys.stdout
        #proc.expect('ftp> ')
        #proc.wait()

        x1 = proc.after
        x2 = proc.before
        x3 = proc.buffer

        proc.close()
        return

    # TODO clean CMake cache
    # TODO Run cmake to process

    # https://pexpect.readthedocs.org/en/latest/overview.html