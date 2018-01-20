import unittest

from src.integration.Equation import Equation
from src.systemInput import SystemVariable


class TestEquation(unittest.TestCase):
    #define Test-Functions
    def test_Equation(self):
        testVar1 = SystemVariable.SystemVariable('Beute', 'Hase/Hasen', 500)
        testVar2 = SystemVariable.SystemVariable('Raeuber', 'Luchs/Luchse', 500)
        testVar3 = SystemVariable.SystemVariable('Treffen', 'Beute*Raeuber', 0)

        e = Equation("Beutewachstum", testVar1, testVar2)

        #Name of the SystemVariable is needed
        e.defineFunction("Beute * 0.01")

        testVar3.addEquation(e)

        testVar1.currentValue = 1000
        testVar2.currentValue = 2000

        testVar3.calculateNewValue()

        print(testVar3.newValue)


#start unittest
if __name__ == '__main__':
    unittest.main()