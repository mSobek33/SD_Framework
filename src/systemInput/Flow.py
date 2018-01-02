from src.systemInput.SystemVariable import SystemVariable, Type

class Flow(SystemVariable):

    def __init__(self, name, unit):
        """
        Define new Flow (if it is input or output is define in SystemVariable)
        :param name: name of the Flow
        :param equation: formula for calculation
        """
        self.name = name
        self.unit = unit
        #self.currentValue = currentValue
        #self.newValue= newValue
        self.type = Type.Type.flow
        #self.inputFlow = list()
        #self.outputFlow = list()
        self.causalEdgeList = list()
        self.currentValue = "" 
        self.newValue = ""
        self.model = ""
        self.valueHistoryList = list()
        # TODO
        self.valueHistoryList.append(None)


