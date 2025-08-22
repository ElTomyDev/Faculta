"""
Ejercicio 4

    Escribir una función que dado una lista de enteros me devuelve otra(no necesariamente en el mismo orden) sin los numeros repetidos.

    Por ejemplo:

    Lista de entrada = [1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]

    Lista de salida = [1 , 3 , 2, 4]

"""
from diccionario import Diccionario

def eliminarRepetidos(lista:list) -> list:
    dic = Diccionario(lista, lista)
    return dic.keys()

print(eliminarRepetidos([2,3,4,5,3,4,2,5,7,4,2,3,7,8,5,5]))