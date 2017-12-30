class Flow:

    def __init__(self, name):
        """
        Define new Flow (if it is input or output is define in SystemVariable)
        :param name: name of the Flow
        :param equation: formula for calculation
        """
        self.name = name
        self.currentValue = 0

    def addEquation(self, equation):
        """
        set Equation
        :return: current Value 
        """
        self.equation = equation
