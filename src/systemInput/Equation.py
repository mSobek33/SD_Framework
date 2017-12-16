import pydoc

class Equation:
    """
    Class to define the Equations for the different Flows
    """
    pass

    def __init__(self, defintion):
        """
        Construct a new Flow-'Evaluation'
        :param defintion: formular 
        """
        self.defintion = defintion


    def calculateValue(self):
        """
        calculate current Value, Current Values must be set before
        :return: current result
        """
        #toDo
        #eval soll die zu dieser Zeit definierten Variablen aus den Klassen lesen
        return eval(self.defintion)
