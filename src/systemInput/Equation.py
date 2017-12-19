import pydoc
import re


class Equation:
    """
    Class to define the Equations for the different Flows
    """
    pass

    def __init__(self, name, *args):
        """
        Construct a new Flow-'Evaluation'
        :param name: set name of function
        :param args: a list (various) of SystemVariables
        """
        self.name = name
        self.listVariable = dict()
        for i in args:
            self.listVariable[i.name] = i


    def defineFunction(self, functionalEquation):
        """
        Define Function
        :return: current result
        """
        # eval soll die zu dieser Zeit definierten Variablen aus den Klassen lesen
        self.functionalEquation = functionalEquation


    def calculateCurrentValue(self):
        """
        Calculate the current Value
        :return: 
        """
        splittedEquation = re.split("([*,+,/,-])", self.functionalEquation.replace(" ", ""))
        counter = 0
        for i in splittedEquation:
            if i in self.listVariable:
                help = self.listVariable[i]
                splittedEquation[counter] = str(help.currentValue)
            counter += 1
        return eval("".join(splittedEquation))
