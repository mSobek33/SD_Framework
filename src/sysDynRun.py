# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import SystemVariable, Type, Model, Level, Constant, Auxiliary, Flow
    from src.integration.Equation import Equation
else:
    from src.systemInput import SystemVariable, Type, Model, Level, Constant, Auxiliary, Flow
    from src.integration.Equation import Equation

testBeute = Level.Level('Beute', 'Hase/Hasen', 500)
testInputFlow = Flow.Flow('Zuwachs', 'Hasen/Woche')
testOutputFlow = Flow.Flow('Verlust', 'Hasen/Woche')
#testVar4 = Auxiliary.Auxiliary('Treffen', 'Hase/Hasen')

#testLevel = Level.Level('Beute', 'Hase/Hasen', 500)

#print(testLevel.name)
#print(testLevel.unit)
#print(testLevel.initialValue)
#print(testLevel.type)

mainModel = Model.Model("Model", 0, 10, 1)

mainModel.addSystemVariable(testBeute)
mainModel.addSystemVariable(testInputFlow)
mainModel.addSystemVariable(testOutputFlow)
#mainModel.addSystemVariable(testVar4)

testBeute.addInputFlow(testInputFlow)
testBeute.addOutputFlow(testOutputFlow)

#mainModel.defineCausalEdge(testVar1, testVar2)

# get the names of the variables from the first CausalEdge item
#print(testVar1.causalEdgeList[0].startVariable.name)
#print(testVar1.causalEdgeList[0].endVariable.name)
#test.getCauses()


inputEquation = Equation("Beutewachstum", testBeute)
inputEquation.defineFunction("0.05 * Beute")

outputEquation = Equation("Beuteverlust", testBeute)
outputEquation.defineFunction("(0.001/1) * Beute")

testInputFlow.addEquation(inputEquation)
testOutputFlow.addEquation(outputEquation)

beuteEquation = Equation("Anzahl_Beute", testInputFlow, testOutputFlow)
beuteEquation.defineFunction("Zuwachs - Verlust")
testBeute.addEquation(beuteEquation)

print(mainModel.listSystemVariable)
mainModel.listSystemVariable.sort(key=lambda x: x.type.value, reverse=False)
print(mainModel.listSystemVariable)
#print(testlist)

mainModel.run()

#print(testVar4.newValue)
#testVar4.addEquation(e)
#testVar4.calculateNewValue()
#print(testVar4.newValue)

#testVar.addCausalEdge()
