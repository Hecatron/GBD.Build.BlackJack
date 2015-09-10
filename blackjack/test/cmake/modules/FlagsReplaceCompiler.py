import unittest, os, sys
from blackjack.cmake.modules.FlagsReplaceCompiler import FlagsReplaceCompiler

class Test_FlagsReplaceCompiler(unittest.TestCase):

    def test_global(self):
        flagsect1 = FlagsReplaceCompiler([["/MD","/MT"], ["/Flag1","/Flag2"]])
        result = flagsect1.render()
        print(result)
        if result != ['## Flags Replace Macro', 'set( CompilerFlags ', '    "CMAKE_CXX_FLAGS"',
                      '    "CMAKE_CXX_FLAGS_DEBUG"', '    "CMAKE_CXX_FLAGS_RELEASE"', '    "CMAKE_C_FLAGS"',
                      '    "CMAKE_C_FLAGS_DEBUG"', '    "CMAKE_C_FLAGS_RELEASE"', ')', 'foreach(CompilerFlag )',
                      '  string(REPLACE "/MD" "/MT" ${CompilerFlag} "${${CompilerFlag}}")',
                      '  string(REPLACE "/Flag1" "/Flag2" ${CompilerFlag} "${${CompilerFlag}}")', 'endforeach()']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
