from src.systemInput.SystemVariable import SystemVariable, Type

class Flow(SystemVariable):

    def __init__(self, name, unit):
        """
        Define new Flow (if it is input or output is define in SystemVariable)
        :param name: name of the Flow
        :param equation: formula for calculation
        """
        #SystemVariable.__init__(name, unit)
        self.name = name
        self.unit = unit
        self.type = Type.Type.flow
        self.causalEdgeList = list()
        self.currentValue = "" 
        self.newValue = ""
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