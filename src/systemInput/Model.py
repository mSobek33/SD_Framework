import pydoc

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import CausalEdge, Type
    from src.integration import EulerCauchyIntegration
    from src.diagram import GraphicalUserInterface
else:
    from src.systemInput import CausalEdge, Type
    from src.integration import EulerCauchyIntegration
    from src.diagram import GraphicalUserInterface


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
                print("The variable '" + systemVariable.name + "' already exists!")
                return          
        #toDO
        # EXCEPTION HANDLING? > Abfrage ob Typ passend
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
        
        #Important, flow and auxiliary has to be caluculated bevor level
        self.listSystemVariable.sort(key=lambda x: x.type.value, reverse=False)
        
        while time<self.timeboundary:

            for currentVariable in self.listSystemVariable:
                if currentVariable.type == Type.Type.level:
                    eci = EulerCauchyIntegration.EulerCauchyIntegration()
                    eci.integrate(self.timestep, currentVariable)
                    currentVariable.valueHistoryList.append(currentVariable.newValue)
                elif currentVariable.type == Type.Type.flow or currentVariable.type == Type.Type.auxiliary:
                    currentVariable.calculateNewValue()
                    currentVariable.valueHistoryList.append(currentVariable.newValue)
                    currentVariable.currentValue = currentVariable.newValue

            #set value currentValue = newValue
            for variable in self.listSystemVariable:
                if variable.type == Type.Type.level:
                    variable.currentValue = variable.newValue
    
            time +=1

        #draw and show diagrams
        gui = GraphicalUserInterface.GraphicalUserInterface()
        gui.drawGraphic(self)