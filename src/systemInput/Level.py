
if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from systemInput import Flow
    from systemInput.SystemVariable import SystemVariable
else:
    from systemInput import Flow
    from systemInput.SystemVariable import SystemVariable

class Level(SystemVariable):
    """
    Class to define levels in a system dynamic simulation model.
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
        self.valueHistoryList = list()
        self.valueHistoryList.append(initialValue)
        self.outputFlow =""
        self.initialValue=""
        self.calcPriority = 4

    def addOutputFlow(self, outputflow):
        """
        Add new output Flow 
        :param outputflow: 
        """
        if isinstance(outputflow, Flow.Flow):
            self.outputFlow = outputflow
        else:
            raise Exception("OUTPUTFLOW FROM " + self.name + " MUST BE FLOW")


    def addInputFlow(self, inputflow):
        """
        Add new input Flow
        :param outputflow: 
        :return: 
        """
        if isinstance(inputflow, Flow.Flow):
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
        