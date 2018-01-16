import pydoc

from src.systemInput.SystemVariable import SystemVariable, Type

class Level(SystemVariable):
    
    def __init__(self, name, unit, initialValue):
        #SystemVariable.__init__(name, unit)
        self.name = name
        self.unit = unit
        self.initialValue = initialValue
        self.currentValue = initialValue
        self.newValue= initialValue
        self.type = Type.Type.level
        self.causalEdgeList = list()
        self.model = ""
        self.valueHistoryList = list()
        self.valueHistoryList.append(initialValue)
        self.outputFlow =""
        self.initialValue=""
        
        
    def addOutputFlow(self, outputflow):
        """
        Add new output Flow in list
        :param outputflow: 
        """
        self.outputFlow = outputflow


    def addInputFlow(self, inputflow):
        """
        Add new input Flow in list
        :param outputflow: 
        :return: 
        """
        self.inputFlow = inputflow


    def addEquation(self, equation):
        """
        set equation, just if the SystemVariable is no level
        :param equatition: define function
        :return: 
        """
        self.equation = equation


    def calculateChange(self):
        """
        Aktuellen Wert aus Flüssen berechnen
        :return: 
        """
        if hasattr(self, 'equation'):
            #Abfrage ob inhalte mit Flows uerbeinstimmern
            return self.equation.calculateNewValue()
        else:
            raise Exception("EQUATION MUST BE DEFINED: "+self.name)
        