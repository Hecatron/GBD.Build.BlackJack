import unittest, os, sys
from blackjack.cmake.target.ExeTarget import ExeTarget
from blackjack.cmake.storage.SetList import SetList

class Test_ExeTarget(unittest.TestCase):

    def test_render(self):
        exetgt = ExeTarget("exe target", ["Test1.cpp", "Test2.cpp"], True, True, True)
        result = exetgt.render()
        print(result)
        if result != ['## Executable Target - Normal', 'add_executable(exe_target WIN32 MACOSX_BUNDLE EXCLUDE_FROM_ALL ',
                      '    "Test1.cpp" ', '    "Test2.cpp" )']:
            self.fail("Unexpected result")
        return

    def test_render2(self):
        exetgt = ExeTarget("exe target", ["Test1.cpp", "Test2.cpp"], True, True, True)
        set1 = SetList("set1",["Test1.cpp", "Test2.cpp"])
        exetgt.SetLists.append(set1)
        result = exetgt.render()
        print(result)
        if result != ['## Executable Target - Normal', '## Source Set', 'set(set1 ', '    "Test1.cpp"',
                      '    "Test2.cpp")', 'add_executable(exe_target WIN32 MACOSX_BUNDLE EXCLUDE_FROM_ALL ',
                      '    "set1" ', '    "Test1.cpp" ', '    "Test2.cpp" )']:
            self.fail("Unexpected result")
        return


if __name__ == '__main__':
    unittest.main()
