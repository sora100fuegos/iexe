import warnings
import unittest


def  fixture_ex_5():
       lista = ["maria_1","juan_3","oscar_2","julie_4","christian_5","josh_6","raul_7","ricardo_8","martin_9","citlali_10"]
       return lista

class pruebasact5(unittest.TestCase):
     def salida_dic(self,res):
       self.assertTrue(len(res.keys())==10)
     def dic_ent(self,res):
      nlista=[]
     
      
      for s in list(res.keys()) :
       if(isinstance(s, int)or s.isdigit()):
         nlista.append(s)
    
      self.assertTrue(len(nlista)==len(res.keys()))
  
     def val_string(self,res):
       lista = [value for value in res.values() if(isinstance(value, str))]
       
       self.assertTrue(len(lista)==len(res.values()))