"""
Ejercicio 4

    Escribir una función recursiva que calcule el número triangular de índice N. El número triangular de índice N 
    es la suma de todos los números desde 1 hasta N.

    Algunos ejemplos:

        T(1) = 1

        T(2) = 3 = 1 + 2

        T(3) = 6 = 1 + 2 + 3

        T(4) = 10 = 1 + 2 + 3 + 4

        T(5) = 15 = 1 + 2 + 3 + 4 + 5

        ...

        T(N) = 1 + 2 + 3 + 4 + ... + N
"""

def numeroTriangular(N:int) -> int:
    resultado = 0
    if N <= 0:
        return resultado
    else:
        resultado = N + numeroTriangular(N-1)
    return resultado

print(numeroTriangular(4))