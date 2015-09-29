#! python3

import sys, os, logging
#Uncomment below to use outside of VS for development
sys.path.insert(0, os.path.abspath("../"))
#sys.path.insert(0, os.path.abspath("../contrib/pexpect/"))

# Setup logging
from blackjack.logs.Logger import Logger
Logger.LogLevel = logging.DEBUG
Logger.setup()
log = Logger.getlogger()

try:

    import blackjack.cmake as cmake
    import blackjack.cmake.cmd as cmd
    import blackjack.cmake.cmdpart as cmdpart
    import blackjack.cmake.modules as modules
    import blackjack.cmake.process as process
    import blackjack.cmake.storage as storage
    import blackjack.cmake.target as target
    import blackjack.cmake.vars as vars

    proc1 = process.CMakeProcess()
    #proc1.get_generators()
    #proc1.get_version()
    #proc1.testexe()

    sys.exit(0)
    #sys.path.insert(0, os.path.abspath("./contrib/winpexpect/lib"))
    #sys.path.insert(0, os.path.abspath("./contrib/pexpect"))
    #from process.CMakeProcessOpts import CMakeProcessOpts
    #from helper.Process import Process

    #test1 = CMakeProcessOpts()
    #test1.developer_warnings = False

    #test1.defines = ["test1", "test2"]
    #x = test1.render()
    #log.info(x)

    #x1 = Process()
    #x1.test1()

    #test1 = vars.CMakeBehavior.CMAKE_PROJECT_PROJECT_NAME_INCLUDE("test1")
    #test2 = vars.CMakeBehavior.CMAKE_PROJECT_PROJECT_NAME_INCLUDE("test2")

    #test2._name_ = "123"

    #test3 = vars.CMakeBehavior.BUILD_SHARED_LIBS
    #test33 = vars.CMakeBehavior.CMAKE_ABSOLUTE_DESTINATION_FILES
    #test4 = str(test1)

    xx1 = vars.types.VariableCollection()
    xx1.FullName = "123"

    #test2 = vars.CMakeLangs.CMAKE_COMPILER_IS_GNU("C")
    #test3 = vars.CMakeLangs.CMAKE_COMPILER_IS_GNU("C")

    #test4 = vars.CMakeBuildControl.CMAKE_XCODE_ATTRIBUTE_ATTR("test")


    set1 = storage.SourceList("Test Set")
    set1.add("Test1.cxx")
    set1.add("Test2.cxx")
    set1.add_spacesep("Test3.cxx Test4.cxx")
    set2 = storage.EnvVar("testvar",["testval1", "testval2"])

    sol1 = cmake.Solution("test cmake solution")
    sol1.SourceLists.append(set1)
    sol1.SourceLists.append(set2)
    sol1.IncDirs.append(cmake.src_dir + "/..")
    sol1.IncDirs.append(cmake.src_dir + "/../include")

    flagreplace1 = modules.FlagsReplaceCompiler([["/MD","/MT"], ["/Flag1","/Flag2"]])
    sol1.Footer.append(flagreplace1)

    tgt1 = target.LibTarget("Test Name", [set1, "Test3.c"], target.LibTypes.SHARED)
    sol1.Targets.append(tgt1)

    tgt2 = target.ExeTarget_Imported("Test Name2", True)
    sol1.Targets.append(tgt2)

    result = sol1.render()
    tmp1 = ""

# Output any errors
except Exception as e:
    log.critical (e)
    if Logger.LogLevel == logging.DEBUG:
        import traceback
        traceback.print_exc(file=sys.stdout)
    sys.exit(1)
