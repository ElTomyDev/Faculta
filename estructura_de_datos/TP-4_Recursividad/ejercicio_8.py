"""
Ejercicio 8

    Escribir una función recursiva que calcule la potencia N de un número M (M a la N), ambos números enteros positivos.
    # M⁰ = 1
    # M¹ = m
    # M² = M*M
    # M³ = M*M*M = (M*M) * M = M² * M
    #.....
    # M^N = M*M*....*M (N veces) = M^(N-1) * M

    # N > 0 y M > 0
"""
def calcularPotencia(numero:int, n:int) -> int:
    resultado = numero
    
    if n > 1:
        resultado = resultado * calcularPotencia(numero, n-1)
    return resultado

print(calcularPotencia(2, 5))