# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
from os import path
if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from systemInput import SystemVariable, Type
else:
    from systemInput import SystemVariable, Type

test = SystemVariable.SystemVariable('Beute', 'Hase/Hasen', 500, Type.Type.constant)
print(test.name)
print(test.unit)
print(test.initialValue)
print(test.type)
