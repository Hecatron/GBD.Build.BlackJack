import unittest, os, sys
from blackjack.cmake.storage.SourceList import SourceList

class Test_SourceList(unittest.TestCase):

    def test_basicset(self):
        block1 = SourceList("test set 1", ["Test1.cpp", "Folder1/Test2.cpp"], False)
        block1.add("Test3.cpp")
        block1.add("Test4.cpp")
        block1.add_spacesep("Test5.cpp Test6.cpp Test7.cpp")
        result = block1.render()
        if result != ['## Source Set', 'set(test_set_1 ', '    "Test1.cpp"', '    "Folder1/Test2.cpp"',
                      '    "Test3.cpp"', '    "Test4.cpp"', '    "Test5.cpp"', '    "Test6.cpp"', '    "Test7.cpp"', ')']:
            self.fail("Unexpected result")
        return
        
    def test_parentset(self):
        block1 = SourceList("test set 1", ["Test1.cpp", "Folder1/Test2.cpp"], True)
        block1.add("Test3.cpp")
        block1.add("Test4.cpp")
        block1.add_spacesep("Test5.cpp Test6.cpp Test7.cpp")
        result = block1.render()
        if result != ['## Source Set', 'set(test_set_1 ', '    "Test1.cpp"', '    "Folder1/Test2.cpp"',
                      '    "Test3.cpp"', '    "Test4.cpp"', '    "Test5.cpp"', '    "Test6.cpp"', '    "Test7.cpp"', 'PARENT_SCOPE', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
