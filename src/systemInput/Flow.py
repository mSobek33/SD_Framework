import pydoc

from src.systemInput.Equation import Equation


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
        calculate current Value for the given Equation
        :return: current Value 
        """
        #Testen ob equation von der Richtigen Klassen
        self.equation = equatition
