import warnings
import actividades_3 as prog
def fixture_ex_4():
       lista = [10, 6, 50, 8, 124]
       return lista

import unittest
import actividades_3 as prog
class pruebasact4(unittest.TestCase):
 def digitos(self,res):
    self.assertTrue(res<100)
 def type_error(self,lista):
    self.assertRaises(TypeError,prog.exercise_4(lista), "a")
def type_warning(self, warning, callable, *args, **kwds):
  with warnings.catch_warnings(record=True) as warning_list:
            warnings.simplefilter('always')

            result = callable(*args, **kwds)

            self.assertTrue(any(item.category == warning for item in warning_list))
    