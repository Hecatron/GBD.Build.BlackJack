import unittest, os, sys
from blackjack.cmake.cmdpart.IncludeDir import IncludeDir
from blackjack.cmake.cmdpart.ScopeTypes import ScopeTypes

class Test_IncludeDir(unittest.TestCase):

    def test_global(self):
        incdir1 = IncludeDir(["testdir3/testdir4", "testdir5/testdir6"], ScopeTypes.PUBLIC, True, True)
        result = incdir1.render_global()
        print(result)
        if result != ['    BEFORE SYSTEM ', '    "testdir3/testdir4"', '    "testdir5/testdir6"']:
            self.fail("Unexpected result")
        return

    def test_target(self):
        incdir1 = IncludeDir(["testdir3/testdir4", "testdir5/testdir6"], ScopeTypes.PRIVATE, True, True)
        result = incdir1.render()
        print(result)
        if result != ['SYSTEM BEFORE PRIVATE', '    "testdir3/testdir4"', '    "testdir5/testdir6"']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
