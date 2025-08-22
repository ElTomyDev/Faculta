"""
Ejercicio 3

    Escribir una función que calcule y retorne el factorial
    de un número natural. La operación factorial (!)

"""

def calcular_factorial(numero: int):
    """
    Calcula y devuelve el factorial de (numero).
    """
    factorial = 1
    for n in range(1, numero+1):
        factorial *= n
    return factorial

print(calcular_factorial(6))