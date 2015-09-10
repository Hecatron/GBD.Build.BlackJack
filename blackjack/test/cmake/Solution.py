import unittest, os, sys
from blackjack.cmake.Solution import Solution
from blackjack.cmake.cmdpart.Version import Version
from blackjack.cmake.cmdpart.IncludeDir import IncludeDir
from blackjack.cmake.cmdpart.ScopeTypes import ScopeTypes

class Test_Solution(unittest.TestCase):

    def test_render(self):
        contentsparam = ["TESTVAL1","TESTVAL2"]
        block1 = Solution("Test CMake Project", Version(0,0,1), "C, CXX", Version(2,8,0))

        block1.IncDirs.append("testdir1/testdir2")
        incdir1 = IncludeDir(["testdir3/testdir4", "testdir5/testdir6"], ScopeTypes.PUBLIC, False, False)
        block1.IncDirs.append(incdir1)

        result = block1.render()

        # TODO

        print(result)
        if result != ['## Cachelist Set', 'set( TESTCACHE1 ', '    "TESTVAL1"', '    "TESTVAL2"', '    "TESTVAL3"', '    "TESTVAL4"', '    "TESTVAL5"', 'CACHE STRING "docstring" FORCE', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
