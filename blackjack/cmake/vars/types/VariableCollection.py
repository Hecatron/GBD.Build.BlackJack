from .CMakeVariable import CMakeVariable

class VariableCollectionMeta(type):
    """Metaclass for VariableCollection"""
    
    def __new__(cls, name, bases, namespace, **kwds):
        # Scan for any static properties set to () and set them to a CMakeVariable class automatically
        for nsitem in namespace:
            if namespace[nsitem] == ():
                namespace[nsitem] = CMakeVariable(nsitem)
        result = type.__new__(cls, name, bases, namespace, **kwds)
        return result

class VariableCollection(metaclass=VariableCollectionMeta):
    """Base class for CMake Variable Collections"""

    # TODO Add call to lookup variable via cmake such as APPLE at python runtime
