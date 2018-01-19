import pydoc
from src.systemInput import Type
from src.systemInput.SystemVariable import SystemVariable

class Level(SystemVariable):
    """
    Class to define levels in an system dynamic simulation model.
    """
    
    def __init__(self, name, unit, initialValue):
        """
        Construct a new Level object.
        :param name: Name of the Level
        :param unit: Unit of the values
        :param initialValue: Value for the Level to start the simulation
        """
        SystemVariable.__init__(self, name, unit)
        self.initialValue = initialValue
        self.currentValue = initialValue
        self.newValue= initialValue
        self.type = Type.Type.level
        self.valueHistoryList = list()
        self.valueHistoryList.append(initialValue)
        self.outputFlow =""
        self.initialValue=""

    def addOutputFlow(self, outputflow):
        """
        Add new output Flow 
        :param outputflow: 
        """
        if(outputflow.type == Type.Type.flow):
            self.outputFlow = outputflow
        else:
            raise Exception("OUTPUTFLOW FROM " + self.name + " MUST BE FLOW")


    def addInputFlow(self, inputflow):
        """
        Add new input Flow
        :param outputflow: 
        :return: 
        """
        if (inputflow.type == Type.Type.flow):
            self.inputFlow = inputflow
        else:
            raise Exception("INPUTFLOW FROM " + self.name + " MUST BE FLOW")


    def addEquation(self, equation):
        """
        set equation
        :param equatition: define function
        :return: 
        """
        if hasattr(self, 'inputFlow') and hasattr(self, 'outputFlow'):
            if self.inputFlow.name in equation.listVariable and self.outputFlow.name in equation.listVariable:
                self.equation = equation
            else:
                raise Exception("EQUATION MUST INCLUDE INPUT- AND OUTPUTFLOW OF LEVEL: " + self.name)
        else:
            raise Exception("YOU HAVE TO DEFINE INPUT AND OUTPUTFLOW OF LEVEL: "+self.name)


    def calculateChange(self):
        """
        calculate change of state, current timestep
        :return: new Value
        """
        if hasattr(self, 'equation'):
            return self.equation.calculateNewValue()
        else:
            raise Exception("EQUATION MUST BE DEFINED: "+self.name)
        