
if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from systemInput.SystemVariable import SystemVariable
else:
    from SD_Framework.src.systemInput.SystemVariable import SystemVariable

class Flow(SystemVariable):
    """
    Class to define constants in a system dynamic simulation model.
    """

    def __init__(self, name, unit):
        """
        Construct a new flow object.
        :param name: name of the Flow
        :param unit: Unit of the values
        """
        SystemVariable.__init__(self, name, unit)
        self.currentValue = "" 
        self.newValue = ""
        self.valueHistoryList = list()
        self.valueHistoryList.append(None)
        self.calcPriority = 2

    def addEquation(self, equation):
        """
        set equation
        :param equatition: define function
        :return: 
        """
        for i in list(equation.listVariable.values()):
            if(i in self.getCauses()):
                continue
            else:
                raise Exception("THE VARIABLES DEFINED IN EQUATION " + equation.name + " ARE NOT CONNECTED THROUGH A CAUSALEDGE!")
         
        self.equation = equation

    def calculateNewValue(self):
        """
        Calculate new value, current timestep
        :return: 
        """
        if hasattr(self, 'equation'):
            # self.newValue = self.equation.calculateNewValueByString()
            self.newValue = self.equation.calculateNewValueByLamda()
        else:
            raise Exception("EQUATION MUST BE DEFINED: " + self.name)