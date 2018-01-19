
import pydoc
class SystemVariable:
    """
    Superclass to define SystemVariable in an system dynamic simulation model.
    """

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
        self.causalEdgeList = list()
        self.model = ""

    def addCausalEdge(self, causalEdge):
        """
        Add new causal edge in list
        :param causalEdge: 
        :return: 
        """
        self.causalEdgeList.append(causalEdge)
        
    
    def getCauses(self):
        """
        Get all variables that affect the current value of this variable
        :return: all variables that affect the current value of this variable
        """
        self.causesList = list()
        for i in self.causalEdgeList:
            if(i.endVariable.name != self.name):
                self.causesList.append(i.endVariable)
        return self.causesList
