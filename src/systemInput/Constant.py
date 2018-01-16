import pydoc

from src.systemInput.SystemVariable import SystemVariable, Type

"""
"""

class Constant(SystemVariable):
    
    def __init__(self, name, unit, initalValue):
        #SystemVariable.__init__(name, unit)
        self.name = name
        self.unit = unit
        self.currentValue = initalValue
        self.type = Type.Type.constant
        self.causalEdgeList = list()
        self.model = ""