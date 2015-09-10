import unittest, os, sys
from blackjack.cmake.target.ExeTarget import ExeTarget

class Test_ExeTarget(unittest.TestCase):

    def test_get_objname(self):
        block1 = ExeTarget("exe target", ["Test1.cpp", "Test2.cpp"], True, True, True)
        result = block1.render()
        print(result)
        if result != ['## Executable Target - Normal', 'add_executable(exe_target WIN32 MACOSX_BUNDLE EXCLUDE_FROM_ALL ',
                      '    "Test1.cpp" ', '    "Test2.cpp" ', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
