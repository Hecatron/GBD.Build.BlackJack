import unittest, os, sys
from blackjack.cmake.target.LibTarget_Alias import LibTarget_Alias

class Test_LibTarget_Alias(unittest.TestCase):

    def test_render(self):
        block1 = LibTarget_Alias("lib source", "lib target")
        result = block1.render()
        print(result)
        if result != ['## Library Target - Alias', 'add_library(lib_source ALIAS lib_target', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
