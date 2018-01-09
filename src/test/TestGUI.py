import unittest

from src.integration.Equation import Equation
from src.systemInput.Model import Model
from src.systemInput import SystemVariable, Type, Level
from src.diagram import GraphicalUserInterface


class TestModel(unittest.TestCase):
    #define Test-Functions
    def test_drawGraphic(self):
        model = Model("A", 0, 3, 1)
        beute = Level.Level('Beute', 'Beute', 500)
        raeuber = Level.Level('Raeuber', 'Raeuber', 20)
        model.addSystemVariable(beute)
        model.addSystemVariable(raeuber)

        beuteEquation = Equation("AnzahlBeute", )
        beuteEquation.defineFunction("10")
        beute.addEquation(beuteEquation)

        raeuberEquation = Equation("AnzahlRaeuber", )
        raeuberEquation.defineFunction("5")
        raeuber.addEquation(raeuberEquation)

        model.run()

        gui = GraphicalUserInterface.GraphicalUserInterface()
        gui.drawGraphic(model)

#start unittest
if __name__ == '__main__':
    unittest.main()


