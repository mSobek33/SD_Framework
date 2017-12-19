import unittest

from src.systemInput import SystemVariable, Type
from src.systemInput.Equation import Equation



class TestEquation(unittest.TestCase):
    #define Test-Functions
    def test_Equation(self):
        testVar1 = SystemVariable.SystemVariable('Beute', 'Hase/Hasen', 500, Type.Type.constant)
        testVar2 = SystemVariable.SystemVariable('Raeuber', 'Luchs/Luchse', 500, Type.Type.constant)
        e = Equation("test", testVar1, testVar2)

        #Name of the SystemVariable is needed
        e.defineFunction("Beute*0.01")

        print(e.calculateCurrentValue())

        testVar1.currentValue = 1000

        print(e.calculateCurrentValue())


#start unittest
if __name__ == '__main__':
    unittest.main()