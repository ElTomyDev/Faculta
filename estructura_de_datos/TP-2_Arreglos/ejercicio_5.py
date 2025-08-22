"""
Ejercicio 5

    Desarrollar una función que inserte un elemento en una posición en un vector. 
    Al insertar el elemento, se debe producir un desplazamiento a la derecha de todos
    los elementos en las posiciones siguientes, el último elemento se pierde.

    Por ejemplo:

        v1 = [2, 4, 1, 7, 6, 2]

        insertar(v1, 5, 3) #insertamos un 5 en la posición 3

        => v1 = [2, 4, 1, 5, 7, 6]

"""
import numpy as np

def insertar_elemento_desplazando_elementos(vector: np.array, elemento: int, posicion: int) -> np.ndarray:
    """
    Retorna un vector que es el resultado de remplazar un elemento
    de (vector) en la pocicion (posicion) por (elemento), desplazando
    sus elementos siguientes una pocicion a la derecha sacando tambien el ultimo elemento.
    """
    for index in reversed(range(len(vector))):
        vector[index] = vector[index]
        if index > posicion:
            vector[index] = vector[index-1]
        if index == posicion:
            vector[index] = elemento
        

mi_vector = np.array([2,3,4,5,6,7,8])
insertar_elemento_desplazando_elementos(mi_vector, 8, 2)
print(mi_vector)