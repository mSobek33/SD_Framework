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
        save defined function
        :return: current result
        """
        if "]" and "[" not in functionalEquation:
            self.functionalEquation = functionalEquation
        else:
            raise SyntaxError("USE () INSTEAD OF []")


    def calculateNewValue(self):
        """
        Calculate the new value
        :return: 
        """

        list = ["+", "-", "*", "/", "(", ")"]

        splittedEquation = re.split("([-,*,+,/,(,),])", self.functionalEquation.replace(" ", ""))
        counter = 0
        for i in splittedEquation:
            if i in self.listVariable:
                help = self.listVariable[i]
                splittedEquation[counter] = str(help.currentValue)
            elif any(i in item for item in list):
                pass
            elif self.__is_float(i)==False:
                raise Exception("ATTRIBUTE " + i + " DOES NOT EXIST")
            counter += 1
        return eval("".join(splittedEquation))


    def __is_float(self, input):
        """
        check if a string is a float
        source: https://edumaven.com/python-programming/is-number
        :return: boolean
        """
        try:
            num = float(input)
        except ValueError:
            return False
        return True