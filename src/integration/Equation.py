import re

class Equation:
    """
    Class to define the Equations for the different SystemVariables
    """

    def __init__(self, name, *args):
        """
        Create a new 'Evaluation' object
        :param name: set name of the function
        :param args: a list (various) of SystemVariables
        """
        self.name = name
        self.listVariable = dict()
        for i in args:
            self.listVariable[i.name] = i


    def addCalculationVariable(self, *args):
        """
        Add new Variables to Equation
        :param args: a list (various) of SystemVariables
        :return: nothing
        """
        for i in args:
            self.listVariable[i.name] = i


    def defineFunctionByLambda(self, lambdaExpression):
        """
        save defined lambdaExpression
        :param lambdaExpression: 
        :return: nothing
        """
        if(self.isalambda(lambdaExpression)):
            self.function = lambdaExpression
        else:
            raise Exception("NO LAMBDA-EXPRESSION")



    def calculateNewValueByLamda(self):
        """
        Calculate the new value, current timestep
        :return: 
        """
        return self.function()


    def defineFunctionByString(self, functionalEquation):
        """
        OLD-VERSION WITH STRING-EQUATION
        save defined function
        :return: current result
        """
        if "]" and "[" not in functionalEquation:
            self.functionalEquation = functionalEquation
        else:
            raise SyntaxError("USE () INSTEAD OF []")


    def calculateNewValueByString(self):
        """
        OLD-VERSION WITH STRING-EQUATION
        Calculate the new value, current timestep
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
                raise Exception("ATTRIBUTE " + i + " DOES NOT EXIST, YOU HAVE TO ADD THESE CALCULATION VARIABLE TO EQUATION: " + self.name)
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


    def isalambda(self, expression):
        """
        Check if function is lambda
        Source: https://stackoverflow.com/questions/3655842/how-can-i-test-whether-a-variable-holds-a-lambda
        :return: 
        """
        LAMBDA = lambda: 0
        return isinstance(expression, type(LAMBDA)) and expression.__name__ == LAMBDA.__name__