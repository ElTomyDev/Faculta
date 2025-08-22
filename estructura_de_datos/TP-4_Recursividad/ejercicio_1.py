"""
Ejercicio 1

    Implementar una función que calcule el factorial de un número de forma recursiva

"""

def factorial(N:int)->int:
    fact = None
    if N == 0:
        fact = 1
    else:
        fact = N * factorial(N-1)
    return fact

def factorial_iter(N:int):
    ret = N
    while N > 1:
        N = N - 1
        ret = ret * N
    return ret 

def hola(N:int):
    if N > 1:
        N = hola(N-1)
        print("Hola")
hola(6)
print(factorial_iter(5))


