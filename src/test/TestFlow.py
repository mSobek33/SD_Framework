"""import unittest

from src.systemInput import SystemVariable, Type
from src.systemInput.Flow import Flow


class TestFlow(unittest.TestCase):
    #define Test-Functions
    def test_Equation(self):
        flow = Flow("eingangsrate", "sV.currentValue*0.001")
        sV = SystemVariable.SystemVariable("name", "Meter", 100, Type.Type.constant)
        #FEHLER
        #print(flow.calculateCurrentValue())
        #self.assertEquals(flow.calculateCurrentValue(), 0.1)

#start unittest
if __name__ == '__main__':
    unittest.main()
"""