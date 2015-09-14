from blackjack.cmake.ScriptBase import ScriptBase

class BaseModule(ScriptBase):
    """Base class for all cmake inbuilt modules"""

    def get_modulename(self):
        """
        Returns the name of the class for include()
        Can be overriden if the class name doesn't match the module name
        """
        return self.__class__.__name__

    # TODO add method for getting the include statement
