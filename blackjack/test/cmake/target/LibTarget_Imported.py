import unittest, os, sys
from blackjack.cmake.target.LibTarget_Imported import LibTarget_Imported
from blackjack.cmake.target.LibTypes import LibTypes

class Test_LibTarget_Imported(unittest.TestCase):

    def test_render(self):
        block1 = LibTarget_Imported("lib target1", LibTypes.STATIC, True)
        result = block1.render()
        print(result)
        if result != ['## Library Target - Imported', 'add_library(lib_target1 STATIC IMPORTED GLOBAL)']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
