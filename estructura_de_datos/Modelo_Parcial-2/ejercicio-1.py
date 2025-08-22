"""
    Escribir una función intercambiaClaveValor(diccionario) que recibe un diccionario y retorna otro intercambiando las claves con los valores del original. Si en el diccionario original hay un valor duplicado, en el diccionario de salida queda como clave y como valor se debe poner una lista con las claves originales.

    Se debe resolver usando las operaciones del TDA Diccionario que vimos en clase, sin violar el encapsulamiento ni utilizando estructuras auxiliares. Si es necesario definir funciones auxiliares. No se aceptarán soluciones que no creen ni utilicen el diccionario.

    Ejemplo:

    si dic1 = { (1, 2) , (2, 3) , (4, 2) , (3, 1) , (8, 9) , (7, 1) }

    entonces al invocar intercambiaClaveValor(dic1) se retorna: { (2 , [1 , 4]) , (3 , [2]) , (1 , [3 , 7]) , (9 , [8]) }
"""
from dic.diccionario import Diccionario

class Dic(Diccionario):
    def intercambiaClaveValor(dic):
        pass