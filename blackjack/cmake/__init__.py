# This represents the root of the Sections
# Typically this code pieces together CMakeLists.txt files using Class's that inherit from ScriptBase

# Class Imports
from .ScriptBase import ScriptBase
from .Solution import Solution

# Constants
src_dir = "${CMAKE_CURRENT_SOURCE_DIR}"
