from .types.AutoEnum import AutoEnum

class CompilerIds(AutoEnum):
    """Type of Compiler ID used within CMake"""

    Absoft = ()
    """Absoft Fortran (absoft.com)"""

    ADSP = ()
    """Analog VisualDSP++ (analog.com)"""

    AppleClang = ()
    """Apple Clang (apple.com)"""

    Clang = ()
    """LLVM Clang (clang.llvm.org)"""

    Cray = ()
    """Cray Compiler (cray.com)"""

    Embarcadero = ()
    """Embarcadero (embarcadero.com)"""
    Borland = (-1)
    """Embarcadero (embarcadero.com)"""

    G95 = ()
    """G95 Fortran (g95.org)"""

    GNU = ()
    """GNU Compiler Collection (gcc.gnu.org)"""

    HP = ()
    """Hewlett-Packard Compiler (hp.com)"""

    Intel = ()
    """Intel Compiler (intel.com)"""

    MIPSpro = ()
    """SGI MIPSpro (sgi.com)"""

    MSVC = ()
    """Microsoft Visual Studio (microsoft.com)"""

    OpenWatcom = ()
    """Open Watcom (openwatcom.org)"""

    PGI = ()
    """The Portland Group (pgroup.com)"""

    PathScale = ()
    """PathScale (pathscale.com)"""

    SDCC = ()
    """Small Device C Compiler (sdcc.sourceforge.net)"""

    SunPro = ()
    """Oracle Solaris Studio (oracle.com)"""

    TI = ()
    """Texas Instruments (ti.com)"""

    TinyCC = ()
    """Tiny C Compiler (tinycc.org)"""

    XL = ()
    """IBM XL (ibm.com)"""
    VisualAge = (-1)
    """IBM XL (ibm.com)"""
    zOS = (-1)
    """IBM XL (ibm.com)"""
