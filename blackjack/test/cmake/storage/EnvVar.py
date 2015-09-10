import unittest, os, sys
from blackjack.cmake.storage.EnvVar import EnvVar

class Test_EnvVar(unittest.TestCase):

    def test_render(self):
        contentsparam = ["TESTVAL1","TESTVAL2"]
        block1 = EnvVar("TESTENV1", contentsparam)
        block1.add("TESTVAL3")
        block1.add_spacesep("TESTVAL4 TESTVAL5")
        result = block1.render()
        print(result)
        if result != ['## EnvVar Set', 'set( ENV{TESTENV1} ', '    "TESTVAL1"', '    "TESTVAL2"',
                      '    "TESTVAL3"', '    "TESTVAL4"', '    "TESTVAL5"', ')']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
