import unittest, os, sys
from blackjack.cmake.cmdpart.Version import Version

class Test_Version(unittest.TestCase):

    def test_render(self):
        incdir1 = Version(1,2,3,4)
        result = incdir1.render()
        if result != ['VERSION 1.2.3.4']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
