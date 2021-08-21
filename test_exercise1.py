
import actividades_3 as prog
import unittest

class pruebasact1(unittest.TestCase):  
    
   
 def verificar_entero(self,n):
        
     self.assertTrue(isinstance(n, int))
    
 def verificar_menor_12(self,n):   
   self.assertTrue( n<12,"n should be less than 12")
  
 def elemento_suma(self,res,n): 
  n1= prog.exercise_1(n-1)  
  n2=  prog.exercise_1(n-2) 
  res2 = n1+n2
  self.assertTrue( res==res2,"the elements are not the same")
  
