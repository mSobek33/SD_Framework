# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pydoc

class CausalEdge:
    
    """
    Class to define CausalEdges between two SystemVariables in a system dynamic simulation model.
    """
    
    def __init__(self, startVariable, endVariable):
        """
        Construct a new 'CasualEdge' object.

        :param startVariable: The starting node(from type SystemVariable)
        :param endVariable: The ending node (from type SystemVariable)
        :param influence: positive or negative influence
        :return: returns nothing
        """
        self.startVariable = startVariable
        self.endVariable = endVariable
        
        if(startVariable.model == endVariable.model):
            startVariable.addCausalEdge(self)
            endVariable.addCausalEdge(self)
        else:
            raise ValueError("Both variables must be in the same model.")