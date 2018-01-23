
if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from systemInput.SystemVariable import SystemVariable
else:
    from systemInput.SystemVariable import SystemVariable

class Constant(SystemVariable):
    """
    Class to define constants in a system dynamic simulation model.
    """
    
    def __init__(self, name, unit, initalValue):
        """
        Construct a new constant object.
        :param name: Name of the Auxiliary
        :param unit: Unit of the values
        :return: returns nothing
        """
        SystemVariable.__init__(self, name, unit)
        self.currentValue = initalValue
        self.calcPriority = 3