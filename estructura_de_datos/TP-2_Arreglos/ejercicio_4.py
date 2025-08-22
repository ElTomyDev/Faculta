"""
Ejercicio 4

    Escribir una función que recibe un vector y desplaza todos sus elementos una 
    posición hacia la derecha: el primero pasa a ser el segundo, el segundo pasa a ser el 
    tercero y así sucesivamente. El último pasa a ser el primero.

    Por ejemplo:

        v1 = [2, 4, 1, 5, 7, 9]

        desplazarADerecha(v1)

        => v1 = [9, 2, 4, 1, 5, 7]

"""
import numpy as np

def desplazar_a_derecha(vector):
    """
    Retorna un vector que es el resultado de desplazar
    todos los elementos de (vector) una pocicion hacia la derecha
    """
    desplazado = np.zeros(len(vector), int)
    for index in range(len(vector)):
        desplazado[index] = vector[index-1]
    return desplazado

mi_vector = np.array([2,3,4,5])

print(f"""
        Vector usado: {mi_vector}
        Vector desplazado: {desplazar_a_derecha(mi_vector)} 
    """)