import unittest, os, sys
from blackjack.cmake.target.LibTarget_Object import LibTarget_Object
from blackjack.cmake.target.LibTypes import LibTypes
from blackjack.cmake.storage.SourceList import SourceList

class Test_LibTarget_Object(unittest.TestCase):

    def test_render(self):
        block1 = LibTarget_Object("lib target1", ["Test1.cpp", "Test2.cpp"])
        result = block1.render()
        print(result)
        if result != ['## Library Target - Object', 'add_library(lib_target1 OBJECT', '    "Test1.cpp" ', '    "Test2.cpp" )']:
            self.fail("Unexpected result")
        return

    def test_render2(self):
        libtgt = LibTarget_Object("lib target1", ["Test1.cpp", "Test2.cpp"])
        set1 = SourceList("set1",["Test1.cpp", "Test2.cpp"])
        libtgt.SourceLists.append(set1)
        result = libtgt.render()
        print(result)
        if result != ['## Library Target - Object', '## Source Set', 'set(set1 ', '    "Test1.cpp"', '    "Test2.cpp")',
                      'add_library(lib_target1 OBJECT', '    "set1" ', '    "Test1.cpp" ', '    "Test2.cpp" )']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
