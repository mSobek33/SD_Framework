# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from src.systemInput import SystemVariable, Type, Model, Level, Constant, Auxiliary
    from src.integration.Equation import Equation
else:
    from src.systemInput import SystemVariable, Type, Model, Level, Constant, Auxiliary
    from src.integration.Equation import Equation

testVar1 = Level.Level('Beute', 'Hase/Hasen', 500)
testVar2 = Level.Level('Raeuber', 'Luchs/Luchse', 500)
testVar3 = Level.Level('Beute', 'Hase/Hasen', 500)
testVar4 = Auxiliary.Auxiliary('Treffen', 'Hase/Hasen')

testLevel = Level.Level('Beute', 'Hase/Hasen', 500)

#print(testLevel.name)
#print(testLevel.unit)
#print(testLevel.initialValue)
print(testLevel.type)

mainModel = Model.Model("Model", 1, 500, 10)

mainModel.addSystemVariable(testVar1)
mainModel.addSystemVariable(testVar2)
mainModel.addSystemVariable(testVar3)
mainModel.addSystemVariable(testVar4)


mainModel.defineCausalEdge(testVar1, testVar2)

# get the names of the variables from the first CausalEdge item
print(testVar1.causalEdgeList[0].startVariable.name)
print(testVar1.causalEdgeList[0].endVariable.name)
testVar1.getCauses()


e = Equation("Beutewachstum", testVar1, testVar2)

#Name of the SystemVariable is needed
e.defineFunction("Beute * Raeuber")

print(testVar4.newValue)
testVar4.addEquation(e)
testVar4.calculateNewValue()
print(testVar4.newValue)

#testVar.addCausalEdge()
