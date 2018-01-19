"""
Testclass 
Raueber-Beute-System
"""
if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import SystemVariable, Type, Model, Level, Constant, Auxiliary, Flow
    from src.integration.Equation import Equation
else:
    from src.systemInput import SystemVariable, Type, Model, Level, Constant, Auxiliary, Flow
    from src.integration.Equation import Equation

#Define Level, Auxiliary, Flow and Constant

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


#Define Model
#Put SystemVariable


mainModel = Model.Model("Model", 0, 100, 10)

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


#Define Input and Output-Flows

beute.addInputFlow(beutezuwachs)
beute.addOutputFlow(beuteverlust)
raeuber.addInputFlow(raeuberzuwachs)
raeuber.addOutputFlow(energieverlust)


#Define Equations
inputEquationBeute = Equation("Beutewachstum", wachstumsrateBeute,beute)
inputEquationBeute.defineFunction("WachstumsrateBeute*Beute*(1-(Beute/Weidekapazitaet))")
inputEquationBeute.addCalculationVariable(weidekapazitaet)

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

#Run Model
mainModel.run()


