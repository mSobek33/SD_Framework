import pydoc

from src.systemInput.SystemVariable import SystemVariable, Type

"""
Wir sollten LEVEL, AUXILIARY and CONSTANT als Kindklassen von SystemVariable definieren.
Probeme die ich sehe bspw. LEVEL braucht keine Gleichung
Type auxiliary braucht keinen Startwert
durch die jetztige Beschriebung können auch an Constanten Flows angegangen werden
Konstanten müssen sehr aufwädig definiert werden, obwohl sie so einfach sind.
Wenn wir das so belassen wie jetzt, müssten wir alles mit Typabfragen abfangen 
Können bereits definierte Methoden dann in die einzelnen Klassen packen
"""


class Level(SystemVariable):
    
    def __init__(self, name, unit, initialValue):
        self.name = name
        self.unit = unit
        self.initialValue = initialValue
        self.currentValue = initialValue
        self.newValue= initialValue
        self.type = Type.Type.level
        # muss das eine Liste sein?
        self.inputFlow = list()
        self.outputFlow = list()
        self.causalEdgeList = list()
        self.model = ""
        
        
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