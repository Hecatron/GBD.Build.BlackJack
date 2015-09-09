import unittest, os, sys
from blackjack.cmake.storage.CacheList import CacheList
from blackjack.cmake.storage.CacheTypes import CacheTypes

class Test_CacheList(unittest.TestCase):

    def test_render(self):
        contentsparam = ["TESTVAL1","TESTVAL2"]
        block1 = CacheList("TESTCACHE1", contentsparam, CacheTypes.STRING, "docstring", True)
        block1.add("TESTVAL3")
        block1.add_spacesep("TESTVAL4 TESTVAL5")
        result = block1.render()
        if result != ['## Cachelist Set', 'set( TESTCACHE1 ', '    "TESTVAL1"', '    "TESTVAL2"', '    "TESTVAL3"', '    "TESTVAL4"', '    "TESTVAL5"', 'CACHE STRING "docstring" FORCE', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
