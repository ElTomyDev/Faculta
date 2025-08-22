"""
Ejercicio 1

    Escribir la función recursiva nVecesOmas(arreglo, buscado, N) que retorna verdadero si el arreglo contiene al número “buscado” repetido “N” veces o más. 
    Soluciones que no sean recursivas** NO** serán tenidas en cuenta.

    Por ejemplo, si: arr1 = [3, 1, 2, 4, 3, 6, 7, 3], entonces

        nVecesOmas(arr1, 3, 1) -> True

        nVecesOmas(arr1, 3, 2) -> True

        nVecesOmas(arr1, 3, 4) -> False

        Ayuda: Un número se encuentra cero veces o más en cualquier arreglo (incluso si está vacío)
"""
import numpy as np

def contarVeces(arr, buscado):
    encontrados = 0
    arr_aux = np.array(arr)
    
    if len(arr_aux) > 0:
        if buscado not in arr_aux:
            encontrados = 1 + contarVeces(arr_aux[:len(arr_aux) - 1], buscado)
        else:
            return contarVeces(arr_aux[:len(arr_aux) - 1], buscado)
        return encontrados
    return encontrados

def nVecesOMas(arr, buscado, N):
    return contarVeces(arr, buscado) == N


    




mi_vector = [2,3,4,5,6,7,4]
print(nVecesOMas2(mi_vector, 4, 2))