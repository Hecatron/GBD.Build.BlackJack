from .FlagsReplace import FlagsReplace

class FlagsReplaceCompiler(FlagsReplace):

    """
    Helper Class to replace Compiler Flags within all the Compiler variables

    An Example of how to use this:
    flagreplace1 = modules.FlagsReplaceCompiler([["/MD","/MT"], ["/Flag1","/Flag2"]])
    sol1.Footer.append(flagreplace1)
    """

    def __init__(self, replacements: []):
        # Define list of common CFlag Variables
        flagvars = ["CMAKE_CXX_FLAGS", "CMAKE_CXX_FLAGS_DEBUG", "CMAKE_CXX_FLAGS_RELEASE"]
        flagvars += ["CMAKE_C_FLAGS", "CMAKE_C_FLAGS_DEBUG", "CMAKE_C_FLAGS_RELEASE"]
        super().__init__(flagvars, replacements)
        return
