import unittest

from src.systemInput.Equation import Equation



class TestEquation(unittest.TestCase):
    #define Test-Functions
    def test_Equation(self):
        e = Equation("6+a*8")
        print(e.defintion)

        #Definieren der Variablen a
        a = 10
        #Ausführen der Berechnung
        print(eval(e.defintion))


#start unittest
if __name__ == '__main__':
    unittest.main()