from .BaseOpts import BaseOpts

class BuildOpts(BaseOpts):
    """Command line options passed to a cmake process during build"""

    def __init__(self, cmakepath:str = None):
        super().__init__(cmakepath = cmakepath)

        self.Target = None
        """Build the target instead of default targets"""
        self.Config = None
        """For multi-configuration tools, choose config."""
        self.CleanFirst = False
        """Build target 'clean' first, then build."""

        return

    def get_opts(self):
        """Generate cmd line opts for build mode"""
        self.Args = list()
        self.Args.append("--build")
        self.Args.append(self.BuildDirectory)
        if self.Target != None:
            self.Args.append("--target " + self.Target)
            self.Args.append(self.Target)
        if self.Config != None:
            self.Args.append("--config")
            self.Args.append(self.Config)
        if self.CleanFirst:
            self.Args.append("--clean-first")

        return self.Args
