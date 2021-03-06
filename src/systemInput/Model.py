
if __package__ is None:

    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from systemInput import CausalEdge, Level, Flow, Auxiliary
    from integration import EulerCauchyIntegration
else:
    from SD_Framework.src.systemInput import CausalEdge, Level, Flow, Auxiliary
    from SD_Framework.src.integration import EulerCauchyIntegration


class Model:
    """
    Class to create a system dynamic simulation model
    """

    def __init__(self, name, starttime, endtime, timestep):
        """
        Construct a new 'Model' object.
        :param name: define the name of the Model
        :param starttime: define starttime
        :param endtime: define endtime
        :param timesteps: define timesteps, for the simulation
        :return: returns nothing
        """
        self.modelname = name
        self.listSystemVariable = list()
        self.starttime = starttime
        self.endtime = endtime
        self.timestep = timestep


    def addSystemVariable(self, systemVariable):
        """
        Add a new SystemVariable to the model
        :param systemVariable: the new Variable to add
        :return: returns nothing
        """
        for i in self.listSystemVariable:
            if(i.name == systemVariable.name):
                raise Exception("THE VARIABLE '" + systemVariable.name + "' ALREADY EXISTS")
                return
        systemVariable.model = self
        self.listSystemVariable.append(systemVariable)

    def defineCausalEdge(self, startVariable, endVariable):
        """
        Add a new CausalEdge between two SystemVariables in the current model
        :param startVariable: the start variable
        :param endVariable: the end variable
        :param influence: the influence to the values
        :return: returns nothing
        """
        causalEdge = CausalEdge.CausalEdge(startVariable, endVariable)

    def run(self):
        """
        run whole model
        calculate values for every timestep
        including create and display diagrams
        """
        self.timeboundary =  (self.endtime - self.starttime)/self.timestep
        
        time = 0
        

        self.sort()
        
        while time<self.timeboundary:

            for currentVariable in self.listSystemVariable:
                if isinstance(currentVariable, Level.Level):
                    self.__updateList(Flow.Flow)
                    eci = EulerCauchyIntegration.EulerCauchyIntegration()
                    eci.integrate(self.timestep, currentVariable)
                    currentVariable.valueHistoryList.append(currentVariable.newValue)
                elif isinstance(currentVariable, Flow.Flow):
                    currentVariable.calculateNewValue()
                    currentVariable.valueHistoryList.append(currentVariable.newValue)
                elif isinstance(currentVariable, Auxiliary.Auxiliary):
                    currentVariable.calculateNewValue()
                    currentVariable.valueHistoryList.append(currentVariable.newValue)
                    currentVariable.currentValue = currentVariable.newValue

            self.__updateList(Level.Level)
    
            time +=1



    def sort(self):
        """
        Sort Variable list 
        Important: flow and auxiliary has to be caluculated bevor level
        :return: 
        """
        self.listSystemVariable.sort(key=lambda x: x.calcPriority, reverse=False)
        #important Auxiliary sorting correctly
        for variable in self.listSystemVariable:
            if (isinstance(variable, Flow.Flow)) or variable.checked == True:
                return
            for i in variable.getCauses():
                if(isinstance(i, Auxiliary.Auxiliary)) and i.checked == False:
                    newIndex = self.listSystemVariable.index(i)
                    oldIndex = self.listSystemVariable.index(variable)
                    self.listSystemVariable [newIndex] = variable
                    self.listSystemVariable [oldIndex] = i
            variable.checked = True




    def __updateList(self, type):
        """
        update current = newValue
        :param type: 
        :return: 
        """
        for variable in self.listSystemVariable:
            if isinstance(variable, type):
                variable.currentValue = variable.newValue

