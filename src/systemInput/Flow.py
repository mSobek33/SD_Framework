class Flow:

    def __init__(self, name):
        """
        Define new Flow (if it is input or output is define in SystemVariable)
        :param name: name of the Flow
        :param equation: formula for calculation
        """
        self.name = name

    def addEquation(self, equatition):
        """
        set Equation
        :return: current Value 
        """
        self.equation = equatition
