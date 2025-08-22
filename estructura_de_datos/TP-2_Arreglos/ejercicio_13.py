"""
Ejercicio 13

    Escribir una función que recibe una matriz cuadrada (N x N) y calcula la suma de los elementos
    que están por encima de la diagonal principal (excluyendo la diagonal).

    En el ejemplo de la imagen, la función deberia retornar: b + c + f
    
"""
import numpy as np

def sumar_diagonales(matriz:np.ndarray) -> int:
    filas, columnas = matriz.shape
    if filas != columnas:
        raise Exception(f"La matriz debe ser cuadrada y es de {filas}x{columnas}")

    suma = 0
    cantidad_diagonales = 0
    for f in range(filas):
        for c in reversed(range(columnas)):
            if cantidad_diagonales >= filas:
                break
            if f >= c:
                cantidad_diagonales += 1
            else:
                suma += matriz[f][c]
                print(f"se suma {matriz[f][c]} en {f}x{c}, diagonales encontradas: {cantidad_diagonales}")
    return suma
mi_matriz = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]])
print(sumar_diagonales(mi_matriz))
