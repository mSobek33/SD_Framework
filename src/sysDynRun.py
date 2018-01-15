# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.diagram import GraphicalUserInterface

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import SystemVariable, Type, Model, Level, Constant, Auxiliary, Flow
    from src.integration.Equation import Equation
else:
    from src.systemInput import SystemVariable, Type, Model, Level, Constant, Auxiliary, Flow
    from src.integration.Equation import Equation


weidekapazitaet = Constant.Constant('Weidekapazitaet', 'Beute', 300)
wachstumsrateBeute = Constant.Constant('WachstumsrateBeute', '1/Woche', 0.05)
beutezuwachs = Flow.Flow('Beutezuwachs', 'Beute/Woche')
beute = Level.Level('Beute', 'Beute', 500)
beuteverlust = Flow.Flow('Beuteverlust', 'Beute/Woche')
verlustrateBeute = Constant.Constant('VerlustrateBeute', '1/(Woche*Raeuber)', 0.001)

wachstumsrateRaeuber = Constant.Constant('WachstumsrateRaeuber', '1/(Woche*Beute)', 0.0002)
raeuberzuwachs = Flow.Flow('Raeuberzuwachs', 'Raeuber/Woche')
raeuber = Level.Level('Raeuber', 'Raeuber', 50)
energieverlust = Flow.Flow('Energieverlust', 'Raeuber/Woche')
energieverlustrateRaeuber = Constant.Constant('EnergieverlustrateRaeuber', '1/Woche', 0.1)

treffen = Auxiliary.Auxiliary('Treffen', 'Rauber*Beute')
#testVar4 = Auxiliary.Auxiliary('Treffen', 'Hase/Hasen')

#testLevel = Level.Level('Beute', 'Hase/Hasen', 500)

#print(testLevel.name)
#print(testLevel.unit)
#print(testLevel.initialValue)
#print(testLevel.type)

mainModel = Model.Model("Model", 0, 10, 1)

mainModel.addSystemVariable(weidekapazitaet)
mainModel.addSystemVariable(wachstumsrateBeute)
mainModel.addSystemVariable(beutezuwachs)
mainModel.addSystemVariable(beute)
mainModel.addSystemVariable(beuteverlust)
mainModel.addSystemVariable(verlustrateBeute)

mainModel.addSystemVariable(wachstumsrateRaeuber)
mainModel.addSystemVariable(raeuberzuwachs)
mainModel.addSystemVariable(raeuber)
mainModel.addSystemVariable(energieverlust)
mainModel.addSystemVariable(energieverlustrateRaeuber)

mainModel.addSystemVariable(treffen)
#mainModel.addSystemVariable(testVar4)

beute.addInputFlow(beutezuwachs)
beute.addOutputFlow(beuteverlust)
raeuber.addInputFlow(raeuberzuwachs)
raeuber.addOutputFlow(energieverlust)

#mainModel.defineCausalEdge(testVar1, testVar2)

# get the names of the variables from the first CausalEdge item
#print(testVar1.causalEdgeList[0].startVariable.name)
#print(testVar1.causalEdgeList[0].endVariable.name)
#test.getCauses()


inputEquationBeute = Equation("Beutewachstum", wachstumsrateBeute,beute,weidekapazitaet )
inputEquationBeute.defineFunction("WachstumsrateBeute*Beute*(1-(Beute/Weidekapazitaet))")

outputEquationBeute = Equation("Beuteverlust", treffen, verlustrateBeute)
outputEquationBeute.defineFunction("Treffen*VerlustrateBeute")

beutezuwachs.addEquation(inputEquationBeute)
beuteverlust.addEquation(outputEquationBeute)

beuteEquation = Equation("AnzahlBeute", beutezuwachs, beuteverlust)
beuteEquation.defineFunction("Beutezuwachs - Beuteverlust")
beute.addEquation(beuteEquation)



inputEquationRaeuber = Equation("Rauberwachstum", wachstumsrateRaeuber, treffen)
inputEquationRaeuber.defineFunction("WachstumsrateRaeuber*Treffen")

outputEquationRaeuber = Equation("Raeuberverlust", raeuber, energieverlustrateRaeuber)
outputEquationRaeuber.defineFunction("Raeuber*EnergieverlustrateRaeuber")

raeuberzuwachs.addEquation(inputEquationRaeuber)
energieverlust.addEquation(outputEquationRaeuber)

raeuberEquation = Equation("AnzahlRaeuber", raeuberzuwachs, energieverlust)
raeuberEquation.defineFunction("Raeuberzuwachs - Energieverlust")
raeuber.addEquation(raeuberEquation)



treffenEquation = Equation("Treffen", beute, raeuber)
treffenEquation.defineFunction("Beute*Raeuber")
treffen.addEquation(treffenEquation)


#print(mainModel.listSystemVariable)
#mainModel.listSystemVariable.sort(key=lambda x: x.type.value, reverse=False)
#print(mainModel.listSystemVariable)
#print(testlist)

mainModel.run()

gui = GraphicalUserInterface.GraphicalUserInterface()
gui.drawGraphic(mainModel)

#print(testVar4.newValue)
#testVar4.addEquation(e)
#testVar4.calculateNewValue()
#print(testVar4.newValue)

#testVar.addCausalEdge()
