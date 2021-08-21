
import unittest

import actividades_3 as prog


class pruebasact2(unittest.TestCase):
  #Verifica que el parámetro de entrada es string    
  def verificar_string(self,s):    
    self.assertTrue(isinstance(s,str))
    
  #Verifica que si envías un enunciado, el resultado es el enunciado invertido 
  def enunciado_inv(self,res,s):    
    words = s.split()
    
    words.sort(reverse=True)
    words.sort(reverse=True)
    
    print(words.sort(reverse=True))
    self.assertEqual(res, words,"the  words is not inversed")
   #Verifica que si envías un enunciado, el resultado es una palabra invertida
  def palabra_inv(self,string,s):    
    self.assertEqual(string,s[::-1],"la palabra no esta invertida")
    
   
   