"""
    Escribir una función que elimine el elemento que ocupa una determinada posición de un vector. 
    Al eliminar, los elementos a la derecha del eliminado, deben desplazarse a la izquierda un lugar
    y agregar un cero en la última posición.

    Por ejemplo:

        v1 = [4, 3, 5, 8, 6, 7]

        eliminar(v1, 2) #eliminamos el elemento de la posicion 2

        => v1 = [4, 3, 8, 6, 7, 0]

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
        elif index >= posicion :
            vector[index] = vector[index+1]
        else:
            vector[index] = vector[index]
            
    
mi_vector = np.array([1,2,3,4,5])
eliminar_elemento_y_desplzar(mi_vector, 3)
print(mi_vector)