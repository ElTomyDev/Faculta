"""
Ejercicio 5

    Rehacer le ejercicio 4 pero retornando un diccionario en lugar de una lista.

    Por ejemplo:

        Lista de entrada = [1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]

        Diccionario de salida = { (1 , None) , (3 , None) , (4 , None) , (2 , None) }

"""
from diccionario import Diccionario

def eliminarRepetidos(lista:list) -> list:
    dic = Diccionario(lista, lista)

    return Diccionario(dic.keys(), [None for _ in range(len(dic.keys()))])

print(eliminarRepetidos([2,3,4,5,3,4,2,5,7,4,2,3,7,8,5,5]))