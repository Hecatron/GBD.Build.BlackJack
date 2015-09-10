from enum import Enum

class CompilerID(Enum):
    """Type of Compiler ID used within CMake"""

    Absoft = 1
    """Absoft Fortran (absoft.com)"""

    ADSP = 2
    """Analog VisualDSP++ (analog.com)"""

    AppleClang = 3
    """Apple Clang (apple.com)"""

    Clang = 4
    """LLVM Clang (clang.llvm.org)"""

    Cray = 5
    """Cray Compiler (cray.com)"""

    Embarcadero = 6
    """Embarcadero (embarcadero.com)"""
    Borland = 6
    """Embarcadero (embarcadero.com)"""

    G95 = 7
    """G95 Fortran (g95.org)"""

    GNU = 8
    """GNU Compiler Collection (gcc.gnu.org)"""

    HP = 9
    """Hewlett-Packard Compiler (hp.com)"""

    Intel = 10
    """Intel Compiler (intel.com)"""

    MIPSpro = 11
    """SGI MIPSpro (sgi.com)"""

    MSVC = 12
    """Microsoft Visual Studio (microsoft.com)"""

    OpenWatcom = 13
    """Open Watcom (openwatcom.org)"""

    PGI = 14
    """The Portland Group (pgroup.com)"""

    PathScale = 15
    """PathScale (pathscale.com)"""

    SDCC = 16
    """Small Device C Compiler (sdcc.sourceforge.net)"""

    SunPro = 17
    """Oracle Solaris Studio (oracle.com)"""

    TI = 18
    """Texas Instruments (ti.com)"""

    TinyCC = 19
    """Tiny C Compiler (tinycc.org)"""

    XL = 20
    """IBM XL (ibm.com)"""
    VisualAge = 20
    """IBM XL (ibm.com)"""
    zOS = 20
    """IBM XL (ibm.com)"""
