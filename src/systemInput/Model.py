import pydoc

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import CausalEdge, Type
    from src.integration import EulerCauchyIntegration
else:
    from src.systemInput import CausalEdge, Type
    from src.integration import EulerCauchyIntegration


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
        self.timeboundary =  (self.endtime - self.starttime)/self.timestep
        
        i = 0
        
        # Liste nach Typen ordnen (Flows müssen zuerst berechnet werden!
        self.listSystemVariable.sort(key=lambda x: x.type.value, reverse=False)
        
        while i<self.timestep:
            
            for i2 in self.listSystemVariable:
                if i2.type == Type.Type.level:
                    eci = EulerCauchyIntegration.EulerCauchyIntegration()
                    eci.integrate(self.timestep, i2)
                    i2.valueHistoryList.append(i2.newValue)
                    # TODO
                elif i2.type == Type.Type.flow:
                    i2.calculateNewValue()
                    i2.valueHistoryList.append(i2.newValue)
                elif i2.type == Type.Type.auxiliary:
                    i2.calculateNewValue()
                    i2.valueHistoryList.append(i2.newValue)
                    
            for i3 in self.listSystemVariable:
                if i3.type != Type.Type.constant:
                    i3.currentValue = i3.newValue
    
            i +=1
        
        for i4 in self.listSystemVariable:
            if i4.type != Type.Type.constant:
                print(i4.valueHistoryList)