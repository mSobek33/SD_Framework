# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pydoc

class SystemVariable:
    
    pass
    
    def __init__(self, name, unit, initialValue, type):
        """
        Construct a new 'SystemVariable' object.

        :param name: Name of the SystemVariable
        :param unit: Unit of the values
        :param initialValue: Value for the SystemVariable to start the simulation
        :param type: Enumeration for the specific SystemVariable type
        :return: returns nothing
        """
        self.name = name
        self.unit = unit
        self.initialValue = initialValue
        self.currentValue = initialValue
        self.type = type
        self.inputFlow = list()
        self.outputFlow = list()



    def addOutputFlow(self, outputflow):
        """
        Add new output Flow in list
        :param outputflow: 
        """
        self.outputFlow.append(outputflow)



    def addInputFlow(self, inputflow):
            """
            Add new input Flow in list
            :param outputflow: 
            :return: 
            """
            self.input.append(inputflow)



    def calculateCurrentValue(self):
        """
        Aktuellen Wert aus Flüssen berechnen
        :return: 
        """
        pass