from .ScriptBlock import ScriptBlock
import os

class ToolchainFile(ScriptBlock):

    """
    Represents a toolchain script to be loaded prior to cmake processing the main CMakeLists.txt
    This can be used to override compiler detections for cross compiling
    Default export path is changed to CMakeToolChain.txt
    """

    def __init__(self, contents: [] = None):
        super().__init__(contents)
        return

        maindir = os.path.realpath(sys.argv[0])
        if not os.path.isdir(maindir): maindir = os.path.dirname(maindir)
        self.OutputFilePath = os.path.join(maindir, "CMakeToolChain.txt")
        """Default file path for exports and appends"""
        return
