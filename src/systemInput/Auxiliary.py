import pydoc

from src.systemInput import Type
from src.systemInput.SystemVariable import SystemVariable

class Auxiliary(SystemVariable):
    """
    Class to define auxiliaries in an system dynamic simulation model.
    """
    
    def __init__(self, name, unit):
        """
        Construct a new auxiliary object.
        :param name: Name of the Auxiliary
        :param unit: Unit of the values
        :return: returns nothing
        """
        SystemVariable.__init__(self, name, unit)
        self.type = Type.Type.auxiliary
        self.newValue = ""
        self.currentValue = ""
        self.valueHistoryList = list()
        self.valueHistoryList.append(None)


    def addEquation(self, equation):
        """
        set equation
        :param equatition: define function
        :return: 
        """
        self.equation = equation


    def calculateNewValue(self):
        """
        Calculate new value, current timestep
        :return: 
        """
        if hasattr(self, 'equation'):
            self.newValue = self.equation.calculateNewValue()
        else:
            raise Exception("EQUATION MUST BE DEFINED: " + self.name)