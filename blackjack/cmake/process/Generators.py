from blackjack.cmake.vars.types.AutoEnum import AutoEnum

class Generators(AutoEnum):
    """Enum list of cmake generators for convenience"""

    Visual_Studio_14_2015 = ()
    Visual_Studio_14_2015_Win64 = ()
    Visual_Studio_14_2015_ARM = ()

    Visual_Studio_12_2013 = ()
    Visual_Studio_12_2013_Win64 = ()
    Visual_Studio_12_2013_ARM = ()

    Visual_Studio_11_2012 = ()
    Visual_Studio_11_2012_Win64 = ()
    Visual_Studio_11_2012_ARM = ()

    Visual_Studio_10_2010 = ()
    Visual_Studio_10_2010_Win64 = ()
    Visual_Studio_10_2010_IA64 = ()

    Visual_Studio_9_2008 = ()
    Visual_Studio_9_2008_Win64 = ()
    Visual_Studio_9_2008_IA64 = ()

    Visual_Studio_8_2005 = ()
    Visual_Studio_8_2005_Win64 = ()

    Visual_Studio_7_NET_2003 = ()
    Visual_Studio_7 = ()
    Visual_Studio_6 = ()

    Borland_Makefiles = ()
    NMake_Makefiles = ()
    NMake_Makefiles_JOM = ()
    Green_Hills_MULTI = ()
    MSYS_Makefiles = ()
    MinGW_Makefiles = ()
    Unix_Makefiles = ()
    Ninja = ()
    Watcom_WMake = ()

    CodeBlocks_MinGW_Makefiles = ()
    CodeBlocks_NMake_Makefiles = ()
    CodeBlocks_Ninja = ()
    CodeBlocks_Unix_Makefiles = ()
    CodeLite_MinGW_Makefiles = ()
    CodeLite_NMake_Makefiles = ()
    CodeLite_Ninja = ()
    CodeLite_Unix_Makefiles = ()
    Eclipse_CDT4_MinGW_Makefiles = ()
    Eclipse_CDT4_NMake_Makefiles = ()
    Eclipse_CDT4_Ninja = ()
    Eclipse_CDT4_Unix_Makefiles = ()
    KDevelop3 = ()
    KDevelop3_Unix_Makefiles = ()
    Kate_MinGW_Makefiles = ()
    Kate_NMake_Makefiles = ()
    Kate_Ninja = ()
    Kate_Unix_Makefiles = ()
    Sublime_Text_2_MinGW_Makefiles = ()
    Sublime_Text_2_NMake_Makefiles = ()
    Sublime_Text_2_Ninja = ()
    Sublime_Text_2_Unix_Makefiles = ()

    def __str__(self):
        # Replace any underscores with spaces
        ret = str(self.name)
        ret = ret.replace("_", " ")
        ret = ret.replace("CodeBlocks ", "CodeBlocks - ")
        ret = ret.replace("CodeLite ", "CodeLite - ")
        ret = ret.replace("Eclipse_CDT4 ", "Eclipse_CDT4 - ")
        ret = ret.replace("Kate ", "Kate - ")
        ret = ret.replace("Sublime_Text_2 ", "Sublime_Text_2 - ")
        if ret == "KDevelop3 Unix Makefiles": ret = "KDevelop3 - Unix Makefiles"
        if ret == "Visual Studio 7 NET 2003": ret = "Visual Studio 7 .NET 2003"
        return str(ret)
