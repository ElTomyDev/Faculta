"""
Ejercicio 3

Implementar una función recursiva que calcule los números de la serie de Fibonacci. 
La función para generar la serie de Fibonacci es la siguiente (donde N es el índice del número en la serie):

Luego escribir un programa que pida un número N (mayor o igual a 0) al usuario e imprima por pantalla los primeros N números de la serie de Fibonacci

Sobre la sucesion de Fibonacci: https://www.vix.com/es/btg/curiosidades/4461/que-es-la-sucesion-de-fibonacci

"""
import numpy as np

def fibonacci(N:int) -> int:
    if N < 0:
        raise Exception("N debe ser mayor o igual a 0.")
    fibo = 0
    if fibo == 0:
        return fibonacci(N) + 1
    else:
        if N > 1:
            fibo = fibonacci(N-1) + fibonacci(N-2)
            return fibo
    return fibo

print(fibonacci(5))