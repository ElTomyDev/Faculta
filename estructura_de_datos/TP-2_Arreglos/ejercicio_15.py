"""
Ejercicio 15

    Escribir una función que retorna True si una matriz cuadrada de enteros es simétrica y False en caso contrario.

    Una matriz simétrica es como la de la imagen (no importan los elementos de la diagonal principal):

    texto alternativo

    Es decir:

        Si i, j son los índices de las filas y columnas de M

        => Una matriz M es simétrica si:

        M [ i , j ] == M[ j, i ] para todo i != j

        Matriz simétrica de 4 x 4:
                    Col 0 	Col 1 	Col 2 	Col 3
            Fila 0 	2 	    1 	    0 	    5
            Fila 1 	1 	    2 	    9 	    7
            Fila 2 	0 	    9 	    0 	    8
            Fila 3 	5 	    7 	    8 	    4

"""
import numpy as np

def es_simetrica(matriz:np.ndarray) -> bool:
    """
    Indica si (matriz) es o no simetrica.
    """
    for fila in range(matriz.shape[0]):
        for columna in range(matriz.shape[1]):
            if matriz[fila, columna] != matriz[columna, fila]:
                return False
    return True

mi_matriz = np.array([
    [1,1,0],
    [1,1,0],
    [0,0,1]])

print(es_simetrica(mi_matriz))