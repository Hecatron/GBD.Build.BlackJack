import unittest, os, sys
from blackjack.cmake.target.ExeTarget_Alias import ExeTarget_Alias

class Test_ExeTarget_Alias(unittest.TestCase):

    def test_render(self):
        block1 = ExeTarget_Alias("exe source", "exe target")
        result = block1.render()
        print(result)
        if result != ['## Executable Target - Alias', 'add_executable(exe_source ALIAS exe_target)']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
