
import blackjack.contrib.pexpect.wexpect as pexpect
import sys, time

class CMakeProcess(object):
    """Represents a CMake Process that can be called externally"""

    def __init__(self):
        # Assume cmake is in the current path
        self.Version = None
        self.Generators = None
        self.Result = None
        self.ExeSuffix = ""
        if sys.platform == 'win32':
            self.ExeSuffix = ".exe"
        self.CMakePath = "cmake" + self.ExeSuffix

    # TODO clean CMake cache
    # TODO Run cmake to process

    def get_generators(self):
        """Get a list of generators"""
        child = pexpect.spawn(self.CMakePath,["--help"])
        time.sleep(0.1)
        child.expect('The following generators are available on this platform:')
        child.expect(pexpect.EOF)
        child.close()
        result = child.before.replace('\r', '')
        result = result.split("\n")
        resultlist = list()
        for item in result:
            if item == '': continue
            if "=" in item:
                itemsplit = item.split("=")
                itemsplit[0] = itemsplit[0].replace("[arch]", "").strip()
                itemsplit[1] = itemsplit[1].strip()
                resultlist.append([itemsplit[0],itemsplit[1]])
            else:
                resultlist[-1][1] += "\n" + item.strip()

        self.Result = resultlist
        self.Generators = resultlist
        return self.Result

    def get_version(self):
        """Get the Version of CMake"""
        child = pexpect.spawn(self.CMakePath,["--version"])
        child.expect('cmake version ')
        child.expect(pexpect.EOF)
        child.close()
        result = child.before.split('\n')[0]
        result = result.replace('\r', '')
        self.Result = result
        self.Version = result
        return self.Result

    def testexe(self):
        """Test the cmake exe"""
        # Test the CMake exe
        child = pexpect.spawn(self.CMakePath,["--version"])
        # Log everything to stdout
        child.logfile = sys.stdout
        # Tell pexpect to finish processing
        child.expect(pexpect.EOF)
        child.close()
        result = child.before
        self.Result = result
        return self.Result
