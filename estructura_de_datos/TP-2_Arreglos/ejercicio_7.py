"""
    Escribir una función que elimine todas las apariciones de un determinado elemento de un vector. 
    Al eliminar se deben insertar tantos ceros al final como elementos se eliminaron.

    Por ejemplo:

        arr1 = [4, 3, 5, 8, 6, 5, 7, 5]

        eliminarApariciones(arr1, 5) #eliminamos todos los 5 del arreglo

        => arr1 = [4, 3, 8, 6, 7, 0, 0, 0]

"""
import numpy as np

def eliminar_elemento_y_desplzar(vector: np.ndarray, posicion:int):
    """
    Elimina el elemento que esta en la pocicion (posicion)
    del vector (vector) desplazando sus elemento a la izquierda
    dejando un 0 en la ultima posicion.
    """
    for index in range(posicion, len(vector)):
        if index == len(vector)-1:
            vector[index] = 0
        elif index >= posicion:
            vector[index] = vector[index+1]
        else:
            vector[index] = vector[index]

def eliminar_todas_las_apariciones(vector: np.ndarray, elemento:int):
    """
    Elimina todas las apariciones del elemento (elemento) que esta
    en el vector (vector) agregando un 0 al final por cada eliminacion
    """
    while elemento in vector:
        posicion = None
        for index in range(len(vector)):
            if vector[index] == elemento:
                posicion = index
                break
        if posicion != None:
            eliminar_elemento_y_desplzar(vector, posicion)
            posicion = None

mi_vector = np.array([1,4,4,4,5,6,7])
eliminar_todas_las_apariciones(mi_vector, 4)
print(mi_vector)