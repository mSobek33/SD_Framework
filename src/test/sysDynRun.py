"""
Testclass 
Raueber-Beute-System
"""
import unittest

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from systemInput import Model, Level, Constant, Auxiliary, Flow
    from integration.Equation import Equation
    from visualization.ResultVisualization import ResultVisualization
else:
    import sys
    from os import path
    from SD_Framework.src.systemInput import Model, Level, Constant, Auxiliary, Flow
    from SD_Framework.src.integration.Equation import Equation
    from SD_Framework.src.visualization.ResultVisualization import ResultVisualization


class TestSD(unittest.TestCase):
    
    def test(self):
        
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

        #Define Input and Output-Flows

        beute.addInputFlow(beutezuwachs)
        beute.addOutputFlow(beuteverlust)
        raeuber.addInputFlow(raeuberzuwachs)
        raeuber.addOutputFlow(energieverlust)
        

        #Define Model
        #Put SystemVariable
        mainModel = Model.Model("Model", 0, 100, 1)

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

        mainModel.defineCausalEdge(wachstumsrateRaeuber, raeuberzuwachs)
        mainModel.defineCausalEdge(raeuber,energieverlust)
        mainModel.defineCausalEdge(energieverlustrateRaeuber,energieverlust)
        mainModel.defineCausalEdge(raeuber,treffen)
        mainModel.defineCausalEdge(treffen, raeuberzuwachs)
        mainModel.defineCausalEdge(treffen, beuteverlust)

        mainModel.defineCausalEdge(verlustrateBeute, beuteverlust)
        mainModel.defineCausalEdge(beute, treffen)
        mainModel.defineCausalEdge(beute, beutezuwachs)
        mainModel.defineCausalEdge(wachstumsrateBeute, beutezuwachs)
        mainModel.defineCausalEdge(weidekapazitaet, beutezuwachs)

        
        #Define Equations
        inputEquationBeute = Equation("Beutewachstum", wachstumsrateBeute, beute)
        inputEquationBeute.addCalculationVariable(weidekapazitaet)
        inputEquationBeute.defineFunctionByLambda(lambda: wachstumsrateBeute.currentValue * beute.currentValue *
                                                           (1-(beute.currentValue/weidekapazitaet.currentValue)))
        ##inputEquationBeute.defineFunctionByString("WachstumsrateBeute*Beute*(1-(Beute/Weidekapazitaet))")

        outputEquationBeute = Equation("Beuteverlust", treffen, verlustrateBeute)
        #outputEquationBeute.defineFunctionByString("Treffen*VerlustrateBeute")
        outputEquationBeute.defineFunctionByLambda(lambda: treffen.currentValue * verlustrateBeute.currentValue)

        beutezuwachs.addEquation(inputEquationBeute)
        beuteverlust.addEquation(outputEquationBeute)

        beuteEquation = Equation("AnzahlBeute", beutezuwachs, beuteverlust)
        #beuteEquation.defineFunctionByString("Beutezuwachs - Beuteverlust")
        beuteEquation.defineFunctionByLambda(lambda: beutezuwachs.currentValue - beuteverlust.currentValue)
        beute.addEquation(beuteEquation)

        inputEquationRaeuber = Equation("Rauberwachstum", wachstumsrateRaeuber, treffen)
        # inputEquationRaeuber.defineFunctionByString("WachstumsrateRaeuber*Treffen")
        inputEquationRaeuber.defineFunctionByLambda(lambda: wachstumsrateRaeuber.currentValue * treffen.currentValue)

        outputEquationRaeuber = Equation("Raeuberverlust", raeuber, energieverlustrateRaeuber)
        #outputEquationRaeuber.defineFunctionByString("Raeuber*EnergieverlustrateRaeuber")
        outputEquationRaeuber.defineFunctionByLambda(lambda: raeuber.currentValue * energieverlustrateRaeuber.currentValue)

        raeuberzuwachs.addEquation(inputEquationRaeuber)
        energieverlust.addEquation(outputEquationRaeuber)

        raeuberEquation = Equation("AnzahlRaeuber", raeuberzuwachs, energieverlust)
        #raeuberEquation.defineFunctionByString("Raeuberzuwachs - Energieverlust")
        raeuberEquation.defineFunctionByLambda(lambda: raeuberzuwachs.currentValue - energieverlust.currentValue)
        raeuber.addEquation(raeuberEquation)

        treffenEquation = Equation("Treffen", beute, raeuber)
        #treffenEquation.defineFunctionByString("Beute*Raeuber")
        treffenEquation.defineFunctionByLambda(lambda: beute.currentValue * raeuber.currentValue)
        treffen.addEquation(treffenEquation)


        #Run Model
        mainModel.run()
        
        #draw and show diagrams
        gui = ResultVisualization()
        gui.createCSV(mainModel, 'output.csv')
        gui.drawGraphic(mainModel)


        # Unittests
        # Results
        checkListBeute = [500, 458.333, 423.322, 393.631, 368.27]
        checkListRaeuber = [50, 50, 49.5833, 48.8229, 47.7843]
        counter = 0
        for value in raeuber.valueHistoryList[0:5]:
            self.assertAlmostEqual(value, checkListRaeuber[counter], 3)
            counter=counter+1
        
        counter = 0
        for value in beute.valueHistoryList[0:5]:
            self.assertAlmostEqual(value, checkListBeute[counter], 3)
            counter=counter+1


#start unittest
if __name__ == '__main__':
    unittest.main()

