
"""
    3.	La función exercise_3(string, pattern, occurrence) recibe como parámetro un enunciado, una palabra y un número de ocurrencia de la palabra enviada a partir del cual se devuelve el enunciado. Por ejemplo para el enunciado “hoja de palo es diferente a hoja de planta y a hoja de papel”, si el patrón es hoja y la ocurrencia es 2, la función regresa “hoja de planta y a hoja de papel”. Agrega las siguientes pruebas unitarias a tu archivo test_actividades_3.py

     a.	Verifica que recibes dos strings y un entero en ese orden

     b.	Verifica que si envías un string, pattern y occurrence válido obtienes el enunciado de salida correcto

     c.	Verifica que si envías un string, pattern y occurrence donde el pattern no exista en el string, no truene

     d.	Verifica que si envías un string, pattern y occurrence donde el occurrence no exista, no truene.


"""
import unittest
import actividades_3 as prog
class pruebasact3(unittest.TestCase):
    

 #Verifica que recibes dos strings y un entero en ese orden
 def orden(self, s1 , s2  , n =2):         
  res = prog.exercise_3(s1,s2,n)
  self.assertEqual(prog.exercise_3("hoja de palo es diferente a hoja de planta y a hoja de papel","hoja",2),res)
  
 def salida_correcta(self,s1,res):   
  #Verifica que si envías un string, pattern y occurrence válido obtienes el enunciado de salida correcto
  self.assertEqual(s1,res)
  #  c.	Verifica que si envías un string, pattern y occurrence donde el pattern no exista en el string, no truene
  #print(prog.exercise_3(s1,s2,4))
 def existencia(self, s1): 
  self.assertEqual(s1,None)
  #Verifica que si envías un string, pattern y occurrence donde el occurrence no exista, no truene
 def ocur(self,s1):
  self.assertEqual(s1, None)

def testexercise_4(self, lista = [10, 6, 50, 8, 124]):
  return self.assertTrue(isinstance(prog.exercise_4(lista)))