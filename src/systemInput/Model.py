import pydoc

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import CausalEdge
else:
    from src.systemInput import CausalEdge


class Model:

    def __init__(self, name, starttime, endtime, timesteps):
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
        self.timesteps = timesteps


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
        self.listSystemVariable.append(systemVariable)

    def defineCausalEdge(self, startVariable, endVariable, influence):
        """
        Add a new CausalEdge between two SystemVariables in the current model
        :param startVariable: the start variable
        :param endVariable: the end variable
        :param influence: the influence to the values
        :return: returns nothing
        """
        for i in self.listSystemVariable:
            if(i.name == startVariable.name):
                print("The variable '" + startVariable.name + "' already exists!")
                break
            else:
                print("The variable '" + startVariable.name + "' does not exist in the current model!")
                return
            
            if(i.name == endVariable.name):
                print("The variable '" + endVariable.name + "' already exists!")
                break
            else:
                print("The variable '" + endVariable.name + "' does not exist in the current model!")
                return
        causalEdge = CausalEdge.CausalEdge(startVariable, endVariable, influence)
        
    def run(self):
        """
        run whole model
        """
        pass