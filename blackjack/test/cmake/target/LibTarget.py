import unittest, os, sys
from blackjack.cmake.target.LibTarget import LibTarget
from blackjack.cmake.target.LibTypes import LibTypes
from blackjack.cmake.storage.SourceList import SourceList

class Test_LibTarget(unittest.TestCase):

    def test_render(self):
        libtgt = LibTarget("lib target1",["Test1.cpp", "Test2.cpp"], LibTypes.STATIC, True)
        result = libtgt.render()
        print(result)
        if result != ['## Library Target - Normal', 'add_library(lib_target1 STATIC EXCLUDE_FROM_ALL ',
                      '    "Test1.cpp" ', '    "Test2.cpp" )']:
            self.fail("Unexpected result")
        return

    def test_render2(self):
        libtgt = LibTarget("lib target1",["Test1.cpp", "Test2.cpp"], LibTypes.STATIC, True)
        set1 = SourceList("set1",["Test1.cpp", "Test2.cpp"])
        libtgt.SourceLists.append(set1)
        result = libtgt.render()
        print(result)
        if result != ['## Library Target - Normal', '## Source Set', 'set(set1 ', '    "Test1.cpp"',
                      '    "Test2.cpp")', 'add_library(lib_target1 STATIC EXCLUDE_FROM_ALL ', '    "set1" ',
                      '    "Test1.cpp" ', '    "Test2.cpp" )']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
