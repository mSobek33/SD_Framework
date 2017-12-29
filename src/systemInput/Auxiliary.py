import pydoc

from src.systemInput.SystemVariable import SystemVariable,Type

"""
Wir sollten LEVEL, AUXILIARY and CONSTANT als Kindklassen von SystemVariable definieren.
Probeme die ich sehe bspw. LEVEL braucht keine Gleichung
Type auxiliary braucht keinen Startwert
durch die jetztige Beschriebung können auch an Constanten Flows angegangen werden
Konstanten müssen sehr aufwädig definiert werden, obwohl sie so einfach sind.
Wenn wir das so belassen wie jetzt, müssten wir alles mit Typabfragen abfangen :(
"""

class Auxiliary(SystemVariable):
    
    def __init__(self, name, unit):
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
        #self.currentValue = currentValue
        #self.newValue= newValue
        self.type = Type.Type.auxiliary
        #self.inputFlow = list()
        #self.outputFlow = list()
        self.causalEdgeList = list()
        self.newValue = ""