
class SystemVariable:
    """
    Superclass to define SystemVariable in a system dynamic simulation model.
    """

    def __init__(self, name, unit):
        """
        Construct a new 'SystemVariable' object.
        :param name: Name of the SystemVariable
        :param unit: Unit of the values
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
            if(i.startVariable.name != self.name):
                self.causesList.append(i.startVariable)
        return self.causesList
