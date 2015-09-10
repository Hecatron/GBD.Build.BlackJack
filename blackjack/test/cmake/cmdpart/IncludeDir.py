import unittest, os, sys
from blackjack.cmake.cmdpart.IncludeDir import IncludeDir
from blackjack.cmake.cmdpart.ScopeTypes import ScopeTypes
from blackjack.cmake.Solution import Solution
from blackjack.cmake.target.ExeTarget import ExeTarget

class Test_IncludeDir(unittest.TestCase):

    def test_global(self):
        incdir1 = IncludeDir(["testdir3/testdir4", "testdir5/testdir6"], ScopeTypes.PUBLIC, True, True)
        incdir2 = IncludeDir(["testdir3/testdir7", "testdir5/testdir8"])

        sol1 = Solution("test solution1")
        sol1.IncDirs.append(incdir1)
        sol1.IncDirs.append(incdir2)
        sol1.IncDirs.append("testdir5/testdir9")

        result = sol1.render()
        print(result)
        if result != ['## BlackJack Project Defintion', 'cmake_minimum_required(VERSION 2.8)',
                      'project(test_solution1 VERSION 0.0 LANGUAGES C, CXX)', 'include_directories(',
                      '    "testdir5/testdir9")', 'include_directories(', '    BEFORE SYSTEM ', '    "testdir3/testdir4"',
                      '    "testdir5/testdir6")', 'include_directories(', '    "testdir3/testdir7"', '    "testdir5/testdir8")']:
            self.fail("Unexpected result")
        return

    def test_target(self):
        incdir1 = IncludeDir(["testdir3/testdir4", "testdir5/testdir6"], ScopeTypes.PRIVATE, True, True)
        incdir2 = IncludeDir(["testdir3/testdir7", "testdir5/testdir8"])
        incdir3 = "testdir5/testdir9"

        exetgt = ExeTarget("test exe1")
        exetgt.IncDirs.append(incdir1)
        exetgt.IncDirs.append(incdir2)
        exetgt.IncDirs.append(incdir3)

        result = exetgt.render()
        print(result)
        if result != ['## Executable Target - Normal', 'add_executable(test_exe1)', 'target_include_directories( test_exe1',
                      '    PUBLIC "testdir5/testdir9")', 'target_include_directories( test_exe1', 'SYSTEM BEFORE PRIVATE',
                      '    "testdir3/testdir4"', '    "testdir5/testdir6")', 'target_include_directories( test_exe1', 'PUBLIC',
                      '    "testdir3/testdir7"', '    "testdir5/testdir8")']:
            self.fail("Unexpected result")
        return

if __name__ == '__main__':
    unittest.main()
