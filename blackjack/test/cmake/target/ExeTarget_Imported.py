import unittest, os, sys
from blackjack.cmake.target.ExeTarget_Imported import ExeTarget_Imported

class Test_ExeTarget_Imported(unittest.TestCase):

    def test_render(self):
        block1 = ExeTarget_Imported("exe source", True)
        result = block1.render()
        if result != ['## Executable Target - Imported', 'add_executable(exe_source IMPORTED GLOBAL ', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
