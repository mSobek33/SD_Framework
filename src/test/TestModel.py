import unittest

from src.systemInput.Model import Model
from src.systemInput import SystemVariable, Type



class TestModel(unittest.TestCase):
    #define Test-Functions
    def test_addSystemVariable(self):
        model = Model("A", 0, 20, 10)
        length = len(model.listSystemVariable)
        model.addSystemVariable(SystemVariable.SystemVariable("name", "Meter", 100, Type.Type.constant))
        self.assertEquals(len(model.listSystemVariable), length+1)


#start unittest
if __name__ == '__main__':
    unittest.main()
