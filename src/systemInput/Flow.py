import pydoc

from src.systemInput.Equation import Equation


class Flow:

    def __init__(self, name, equation):
        """
        Define new Flow (if it is input or output is define in SystemVariable)
        :param name: name of the Flow
        :param equation: formula for calculation
        """
        self.name = name
        self.equation = Equation(equation)



    def calculateCurrentValue(self):
        """
        calculate current Value for the given Equation
        :return: current Value 
        """
        return self.equation.calculateValue()
