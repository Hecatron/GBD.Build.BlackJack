import sys, os, logging
#Uncomment below to use in VS for development
sys.path.insert(0, os.path.abspath("./"))

# Setup logging
from blackjack.logs.Logger import Logger
Logger.LogLevel = logging.DEBUG
Logger.setup()
log = Logger.getlogger()

try:

    import blackjack.cmake as cmake
    import blackjack.cmake.cmd as cmd
    import blackjack.cmake.cmdpart as cmdpart
    import blackjack.cmake.macros as macros
    import blackjack.cmake.process as process
    import blackjack.cmake.storage as storage
    import blackjack.cmake.target as target

    #sys.path.insert(0, os.path.abspath("./contrib/winpexpect/lib"))
    #sys.path.insert(0, os.path.abspath("./contrib/pexpect"))
    #from process.CMakeProcessOpts import CMakeProcessOpts
    #from helper.Process import Process

    # TODO
    # 1. Read in Visual Studio Project xml files and change to a Target Class
    # 2. Further expansion on set for cache values, enviromnet values
    # 3. Include directories for both target and global, also check Target has a Sets section
    # 4. Document existing code before adding more

    #test1 = CMakeProcessOpts()
    #test1.developer_warnings = False

    #test1.defines = ["test1", "test2"]
    #x = test1.render()
    #log.info(x)

    #x1 = Process()
    #x1.test1()

    #p1 = cmake.ScriptBase()
    #p1.Header.append("Test123")


    store1 = storage.ScriptBlock()
    store1.importfile("D:\\SourceControl\\GitRepos\\GBD.Build.BlackJack\\examples\\testinput.txt")
    x1 = store1.render()


    set1 = storage.SourceList("Test Set")
    set1.add("Test1.cxx")
    set1.add("Test2.cxx")
    set1.add_spacesep("Test3.cxx Test4.cxx")

    sol1 = cmake.Solution("test cmake solution")
    sol1.SourceLists.append(set1)
    sol1.IncDirs.append(cmake.src_dir + "/..")
    sol1.IncDirs.append(cmake.src_dir + "/../include")

    flagreplace1 = macros.FlagsReplaceCompiler([["/MD","/MT"], ["/Flag1","/Flag2"]])
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
