import unittest, os, sys
from blackjack.cmake.target.LibTarget_Interface import LibTarget_Interface
from blackjack.cmake.target.LibTypes import LibTypes

class Test_LibTarget_Interface(unittest.TestCase):

    def test_render(self):
        block1 = LibTarget_Interface("lib target1", True, True)
        result = block1.render()
        print(result)
        if result != ['## Library Target - Interface', 'add_library(lib_target1 INTERFACE IMPORTED GLOBAL', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
