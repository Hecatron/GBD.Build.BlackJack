import unittest, os, sys
from blackjack.cmake.target.LibTarget import LibTarget
from blackjack.cmake.target.LibTypes import LibTypes

class Test_LibTarget(unittest.TestCase):

    def test_render(self):
        block1 = LibTarget("lib target1",["Test1.cpp", "Test2.cpp"], LibTypes.STATIC, True)
        result = block1.render()
        print(result)
        if result != ['## Library Target - Normal', 'add_library(lib_target1 STATIC EXCLUDE_FROM_ALL ',
                      '    "Test1.cpp" ', '    "Test2.cpp" ', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
