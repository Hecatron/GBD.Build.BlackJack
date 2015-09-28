from blackjack.cmake.modules.cmake.BaseModule import BaseModule
from blackjack.cmake.vars.CompilerIds import CompilerIds

class CMakeForceCompiler(BaseModule):

    """
    Inbuilt CMake modules to force C / CXX Compilers for cross compilation
    """

    def __init__(self, lang:str, compilerpath: str, compilerid: CompilerIds):
        super().__init__()
        self._Lang = None
        self.Lang = lang
        """Language for replacing the compiler path"""
        self.CompilerPath = compilerpath
        """Path to the compiler executable"""
        self.CompilerId = compilerid
        """Id of the Compiler"""
        return

    @property
    def Lang(self):
        """Language to operate on"""
        return self._Lang

    @Lang.setter
    def Lang(self, value):
        if value not in ("C", "CXX", "Fortran"):
            raise ValueError("Invalid value for CompilerId")
        self._Lang = value

    @property
    def CompilerId(self):
        """Language to operate on"""
        return self._CompilerId

    @CompilerId.setter
    def CompilerId(self, value):
        if isinstance(value, CompilerID):
            raise ValueError("Invalid value for CompilerId")
        self._CompilerId = value

    def render_body(self):
        ret = ["## CMakeForceCompiler"]
        ret += "CMAKE_FORCE_" + self.Lang + "_COMPILER(" + self.CompilerPath + " " + self.CompilerId + ")"
        return ret
