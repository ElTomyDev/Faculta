"""
Ejercicio 14

    Escribir una función que retorna True si una matriz cuadrada es matriz diagonal y False en caso contrario.

    Una matriz cuadrada diagonal es una matriz que tiene ceros en todos sus elementos, menos en la diagonal 
    principal (No importan los elementos de la diagonal principal, pueden ser cero o no).

    Si i, j son los índices de las filas y columnas de M

    => Una matriz M es diagonal si:

        M [ i , j ] == 0 para todo i != j

        Matriz diagonal de 4 x 4:
                    Col 0 Col 1 Col 2 Col 3
            Fila 0 	0 	  0 	0     0
            Fila 1 	0 	  2 	0     0
            Fila 2 	0 	  0 	4     0
            Fila 3 	0 	  0 	0     0
            
"""
import numpy as np

def es_matriz_cuadrada_diagonal(matriz:np.ndarray) -> bool:
    """
    Indica si (matriz) es o no una matriz cuadrada diagonal.
    """
    filas, columnas = matriz.shape
    
    for f in range(filas):
        for c in range(columnas):
            if f != c:
                if matriz[f][c] != 0:
                    return False
    return True

mi_matriz = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]])

print(es_matriz_cuadrada_diagonal(mi_matriz))
