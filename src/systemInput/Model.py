import pydoc

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
        #EXCEPTION HANDLING? > Abfrage ob Typ passend
        self.listSystemVariable.append(systemVariable)