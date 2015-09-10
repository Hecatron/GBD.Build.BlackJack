# These represent the individual target types for each build destination
# (In Visual Studio terms a CMake Project = Solution, CMake Target = Project)

# All Target Class's inherit from this class
from .BaseTarget import BaseTarget

# Executable Targets
from .ExeTarget import ExeTarget
from .ExeTarget_Alias import ExeTarget_Alias
from .ExeTarget_Imported import ExeTarget_Imported

# Library Targets
from .LibTypes import LibTypes
from .LibTarget import LibTarget
from .LibTarget_Alias import LibTarget_Alias
from .LibTarget_Imported import LibTarget_Imported
from .LibTarget_Interface import LibTarget_Interface
from .LibTarget_Object import LibTarget_Object
