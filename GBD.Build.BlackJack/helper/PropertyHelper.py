# This code can be used to create type constrained properties within Python

def property_type(name, type_, comment = None):

    """
    Generates a Property constrained by a given type
    """
    
    def getter(self):
        return getattr(self, name)
    def setter(self, value):
        if not isinstance(value, type_):
            raise TypeError("%s attribute must be set to an instance of %s" % (name, type_))
        setattr(self, name, value)
    def delete(self):
        delattr(self, name, value)    
    return property(getter, setter, delete, comment)

def property_nontype(name, comment = None):
    
    """
    Generates a Property without type constraints
    """
    
    def getter(self):
        return getattr(self, name)
    def setter(self, value):
        setattr(self, name, value)
    def delete(self):
        delattr(self, name, value)
    return property(getter, setter, delete, comment)
