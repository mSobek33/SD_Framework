# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pydoc
from src.systemInput import Type

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
        self.newValue= initialValue
        self.type = type
        self.inputFlow = list()
        self.outputFlow = list()
        self.causalEdgeList = list()



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
            self.inputFlow.append(inputflow)



    def addCausalEdge(self, causalEdge):
        """
        Add new causal edge in list
        :param causalEdge: 
        :return: 
        """
        self.causalEdgeList.append(causalEdge)



    def addEquation(self, equatition):
        """
        set equation, just if the SystemVariable is no level
        :param equatition: define function
        :return: 
        """
        if self.type != Type.Type.level:
            self.equation = equatition



    def calculateNewValue(self):
        """
        Aktuellen Wert aus Flüssen berechnen
        :return: 
        """
        if hasattr(self, 'equation'):
            self.newValue = self.equation.calculateNewValue()
        else:
            raise Exception("EQUATION MUST BE DEFINED: "+self.name)
