import sys, os, logging
from logs.Logger import Logger

# Setup logging
Logger.LogLevel = logging.INFO
Logger.setup()
log = Logger.getlogger()

try:

    import cmake
    import cmake.macros as macros
    import cmake.cmdpart as cmdpart
    import cmake.target as target

    #sys.path.insert(0, os.path.abspath("./contrib/winpexpect/lib"))
    sys.path.insert(0, os.path.abspath("./contrib/pexpect"))
    #from process.CMakeProcessOpts import CMakeProcessOpts
    #from helper.Process import Process

    # TODO
    # 1. Import an existing txt file into the ScriptBase class - MiddleSection
    # 2. Read in Visual Studio Project xml files and change to a Target Class
    # 3. Further expansion on set for cache values, enviromnet values
    # 4. Write Exe Targets

    #test1 = CMakeProcessOpts()
    #test1.developer_warnings = False

    #test1.defines = ["test1", "test2"]
    #x = test1.render()
    #log.info(x)

    #x1 = Process()
    #x1.test1()

    #p1 = cmake.ScriptBase()
    #p1.Header.append("Test123")

    set1 = cmake.SourceList("Test Set")
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
