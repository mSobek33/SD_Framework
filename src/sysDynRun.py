# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from src.integration.Equation import Equation

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import SystemVariable, Type, Model
else:
    from src.systemInput import SystemVariable, Type, Model

testVar1 = SystemVariable.SystemVariable('Beute', 'Hase/Hasen', 500, Type.Type.constant)
testVar2 = SystemVariable.SystemVariable('Raeuber', 'Luchs/Luchse', 500, Type.Type.constant)
testVar3 = SystemVariable.SystemVariable('Beute', 'Hase/Hasen', 500, Type.Type.constant)
testVar4 = SystemVariable.SystemVariable('Treffen', 'Hase/Hasen', 500, Type.Type.constant)

print(testVar2.name)
print(testVar2.unit)
print(testVar2.initialValue)
print(testVar2.type)

mainModel = Model.Model("Model", 1, 500, 10)

mainModel.addSystemVariable(testVar1)
mainModel.addSystemVariable(testVar2)
mainModel.addSystemVariable(testVar3)
mainModel.addSystemVariable(testVar4)

mainModel.defineCausalEdge(testVar1, testVar2, "positive")

# get the names of the variables from the first CausalEdge item
print(testVar1.causalEdgeList[0].StartVariable.name)
print(testVar1.causalEdgeList[0].EndVariable.name)

e = Equation("Beutewachstum", testVar1, testVar2)

#Name of the SystemVariable is needed
e.defineFunction("Beute * Raeuber")

print(testVar4.newValue)
testVar4.addEquation(e)
testVar4.calculateNewValue()
print(testVar4.newValue)

#testVar.addCausalEdge()
