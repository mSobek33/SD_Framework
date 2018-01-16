import pydoc

from src.systemInput.SystemVariable import SystemVariable,Type

class Auxiliary(SystemVariable):
    
    def __init__(self, name, unit):
        """
        Construct a new 'SystemVariable' object.

        :param name: Name of the SystemVariable
        :param unit: Unit of the values
        :param initialValue: Value for the SystemVariable to start the simulation
        :param type: Enumeration for the specific SystemVariable type
        :return: returns nothing
        """
        # hier constructor superklasse
        #SystemVariable.__init__(name, unit)
        self.name = name
        self.unit = unit
        self.type = Type.Type.auxiliary
        self.causalEdgeList = list()
        self.newValue = ""
        self.currentValue = ""
        self.model = ""
        self.valueHistoryList = list()
        self.valueHistoryList.append(None)


    def addEquation(self, equation):
        """
        set equation, just if the SystemVariable is no level
        :param equatition: define function
        :return: 
        """
        self.equation = equation


    def calculateNewValue(self):
        """
        Calculate new value
        :return: 
        """
        if hasattr(self, 'equation'):
            self.newValue = self.equation.calculateNewValue()
        else:
            raise Exception("EQUATION MUST BE DEFINED: " + self.name)