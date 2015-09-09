import unittest, os, sys
from blackjack.cmake.target.BaseTarget import BaseTarget

class Test_BaseTarget(unittest.TestCase):

    def test_get_objname(self):
        block1 = BaseTarget("base target")
        result = block1.get_objname()
        if result != '$<TARGET_OBJECTS:base_target>':
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
