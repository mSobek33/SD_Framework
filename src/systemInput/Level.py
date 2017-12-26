import pydoc

from src.systemInput.SystemVariable import SystemVariable

"""
Wir sollten LEVEL, AUXILIARY and CONSTANT als Kindklassen von SystemVariable definieren.
Probeme die ich sehe bspw. LEVEL braucht keine Gleichung
Type auxiliary braucht keinen Startwert
durch die jetztige Beschriebung können auch an Constanten Flows angegangen werden
Konstanten müssen sehr aufwädig definiert werden, obwohl sie so einfach sind.
Wenn wir das so belassen wie jetzt, müssten wir alles mit Typabfragen abfangen 
Können bereits definierte Methoden dann in die einzelnen Klassen packen
"""


class Level(SystemVariable):
    pass