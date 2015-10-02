from .BaseOpts import BaseOpts

class BuildOpts(BaseOpts):
    """Command line options passed to a cmake process during build"""

    def __init__(self, cmakepath:str = None):
        super().__init__(cmakepath = cmakepath)

        # TODO

        return

    def get_opts(self):
        """Generate cmd line opts for build mode"""

        self.Args = list()
        self.Args.append("--build")
        self.Args.append(self.BuildDirectory)

        # TODO

        return self.Args

    # TODO options for cmake, for when building after the generation of make files
    # --build <dir>
    # run without options to get list of parameters