"""
Ejercicio 8

    Escribir un procedimiento que reciben un vector y:

        Imprime un subvector con los dos primeros elementos.
        Imprime un subvector con los tres últimos elementos.
        Imprime un subvector con los elementos desde la posiciones 2 hasta la 5
        Imprime un subvector con los elementos alternados cada dos. Por ej.: v1 = [2 , 1 , 4 , 5 , 2 , 7 , 9] debería imprimir [2 , 4 , 2 , 9]

    Nota: Se debe utilizar la notacion vector [ posinicio : posfin : paso ]

"""
import numpy as np


def imprimir_subvectores(vector:np.ndarray):
    """
    Imprime en pantalla los siguientes subvectores:
        - Dos primeros elementos.
        - Tres ultimos elementos.
        - Desde posicion 2 hasta 5
        - Alternados cada dos.
    """
    tamaño = len(vector)
    print(vector)
    print(vector[0:2])
    print(vector[-3:tamaño])
    print(vector[2:5+1])
    print(vector[0:tamaño:2])
    

mi_vector = np.array([1,2,3,4,5,6,7,8,9,0])
imprimir_subvectores(mi_vector)