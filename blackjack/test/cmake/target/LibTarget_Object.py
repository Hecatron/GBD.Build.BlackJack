import unittest, os, sys
from blackjack.cmake.target.LibTarget_Object import LibTarget_Object
from blackjack.cmake.target.LibTypes import LibTypes

class Test_LibTarget_Object(unittest.TestCase):

    def test_render(self):
        block1 = LibTarget_Object("lib target1", ["Test1.cpp", "Test2.cpp"])
        result = block1.render()
        print(result)
        if result != ['## Library Target - Object', 'add_library(lib_target1 OBJECT', '    "Test1.cpp" ', '    "Test2.cpp" ', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
