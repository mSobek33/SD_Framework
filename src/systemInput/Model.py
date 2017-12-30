import pydoc

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import CausalEdge
else:
    from src.systemInput import CausalEdge


class Model:

    def __init__(self, name, starttime, endtime, timestep):
        """
        Construct a new 'Model' object.

        :param modelname: define the name of the Model
        :param listSystemVariable: lists all Nodes (SystemVariable)
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
        #EXCEPTION HANDLING? > Abfrage ob Typ passend
        systemVariable.model = self
        print(systemVariable.model.modelname)
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
        """
        pass