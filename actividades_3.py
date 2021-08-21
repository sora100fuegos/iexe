import re
import warnings


import test_exercise1 as test
import test_exercise2 as test2
import test_exercise3 as test3
import test_exercise4 as test4
import test_exercise5 as test5

def exercise_1(n):
    
    """
    Obtiene el elemento n de la serie de fibonacci: 1, 1, 2, 3, 5, 8, 13, ...

    :param n: posición a regresar de la serie de fibonacci
    :return: elemento n de la serie de fibonacci
    """
    test1 = test.pruebasact1()
    test1.verificar_entero(n)
    test1.verificar_menor_12(n)
        
    if n < 2:
        return n
    else:
        return exercise_1(n-1) + exercise_1(n-2)


def exercise_2(string):
    """
    Si el string tiene varias palabras invierte el orden de las palabras, si el string es una sola palabra la divide
    en letras y las regresa invertidas

    :param string: Word or words to be reversed
    :return: Reverted string
    """
    test = test2.pruebasact2()
    test.verificar_string(string)
    if len(string.split()) > 1:
        words = string.split()
        words.sort(reverse=True)
        
        return words
    else:
        return string[::-1]


def exercise_3(string, pattern, occurrence):
    """
    Obtiene la posición de la eneava ocurrencia de una palabra en un enunciado.

    :param string: Enunciado donde buscar la enevava ocurrencia
    :param pattern: Palabra a buscar
    :param occurrence: Ocurrencia
    :return: Enunciado a partir de la eneava ocurrencia del patrón a encontrar
    """
    
    matches = [element.start() for element in re.finditer(pattern, string)]
    if len(matches) >= occurrence:
        return string[matches[occurrence-1]:]
    else:
        return None


def exercise_4(numbers):
    """
    Divide los numeros entre 2 y devuelve el promedio de los mismos
    :param n: lista de números
    :return: promedio de los números de entrada divididos entre 2
    """
    try:
        pares = [element for element in numbers if element % 2 == 0]

        if len(pares) != len(numbers):
            warnings.warn("los numeros requieren ser pares")
        else:
            pares = [element/2 for element in numbers]
            promedio = sum(pares)/len(pares)

            return promedio

    except TypeError as error:
        print(error)


def exercise_5(elements):
    """
    Genera un diccionario con los elemntos que se envían en una lista. Cada elemento en la lista consiste de un
    string cuyo prefijo es un nombre y el sufijo es un número, el prefijo y sufijo están unidos a través de un guión
    bajo '_'. Por ejemplo: ['maria_1', 'juan_2']

    :param elements: Lista de elementos en formato "palabra_1"
    :return: Diccionario con llaves como los enteros y valores como los strings
    """
    obs = [element.split('_') for element in elements]
    ids = {element[1]: element[0] for element in obs}

    return ids

if __name__ == "__main__":
    exercise_1(11)

class Persona:

    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo


def exercise_6(persona):
    """
    Si es un hombre < 25 años regresar '3.5mg'
    Si es un hombre > 24 años regresar '5mg'
    Si es una mujer < 25 años '2.5mg'
    Si es un hombre > 24 años '4mg'

    :param persona: Instancia de entidad Persona
    :return: Miligramos requeridos por sexo y edad
    """
    if persona.sexo == "H":
        if persona.edad < 25:
            return '3.5mg'
        else:
            return '5mg'
    if persona.sexo == 'M':
        if persona.edad < 25:
            return '2.5mg'
        else:
            return '4mg'

def main():
#test ejercicio  1 

 print(exercise_1(11))
 res = exercise_1(11)
 test1 = test.pruebasact1()
 test1.elemento_suma(res,11)
 
 #test ejercicio  2
 res = exercise_2("hola mundo")
 testex2= test2.pruebasact2()
 testex2.enunciado_inv(exercise_2("hola mundo"),"hola mundo")
 testex2.palabra_inv(exercise_2("hola"),"hola")
  
 #test ejercicio 3
 
 testex3= test3.pruebasact3()
 s1 = "hoja de palo es diferente a hoja de planta y a hoja de papel"
 s2 =  "hoja"
 n = 2 

 testex3.salida_correcta(exercise_3(s1,s2,n), "hoja de planta y a hoja de papel")
 testex3.existencia(exercise_3("hoja de palo es diferente a hoja de planta y a hoja de papel","carlos",2))
 testex3.ocur(exercise_3("hoja de palo es diferente a hoja de planta y a hoja de papel","hoja",5))
 
 
 #test ejercicio 3
 
 testex3= test3.pruebasact3()
 s1 = "hoja de palo es diferente a hoja de planta y a hoja de papel"
 s2 =  "hoja"
 n = 2 

 testex3.salida_correcta(exercise_3(s1,s2,n), "hoja de planta y a hoja de papel")
 testex3.existencia(exercise_3("hoja de palo es diferente a hoja de planta y a hoja de papel","carlos",2))
 testex3.ocur(exercise_3("hoja de palo es diferente a hoja de planta y a hoja de papel","hoja",5))
 
 
 #test ejercicio 4
 numeros = test4.fixture_ex_4()
 testex4= test4.pruebasact4()
 testex4.digitos(exercise_4(numeros))
 lista = ["wdw","xsd"]
 testex4.type_error(lista)
    
 #test ejercicio 5
 numeros = test5.fixture_ex_5()
 testex5= test5.pruebasact5()
 dict = exercise_5(numeros)
 testex5.salida_dic(dict)
 
 my_dict = {'name': 'John', 1: [2, 4, 3]}
 testex5.dic_ent(dict)
 testex5.val_string(dict)
if __name__ == '__main__':
    main()
