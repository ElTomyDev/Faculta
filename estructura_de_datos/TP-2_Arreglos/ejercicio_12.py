"""
Ejercicio 12

    Escribir una función que recibe las dimensiones y retorna una matriz rellena de la siguiente forma: En la posición ( n , m ) debe contener n + m.

    Por ejemplo:

        mat1 = rellenaMatriz(4,3)

        => mat1 =
            Col  0 	Col 1 	Col 2
            Fila 0 	0 	1 	2
            Fila 1 	1 	2 	3
            Fila 2 	2 	3 	4
            Fila 3 	3 	4 	5
"""
import numpy as np

def obtener_matriz_rellena(filas:int, columnas:int) -> np.ndarray:
    """
    Crea y retorna una matriz con (columnas) columnas y (filas) filas
    cuyo relleno es para (c, f) contiene c + f.
    """
    matriz = np.zeros((filas, columnas), int)
    fila, columna = matriz.shape
    for f in range(fila):
        for c in range(columna):
            matriz[f][c] = f + c
    return matriz

print(obtener_matriz_rellena(4,3))