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
        self.Name = name
        self.Unit = unit
        self.InitialValue = initialValue
        self.Type = type