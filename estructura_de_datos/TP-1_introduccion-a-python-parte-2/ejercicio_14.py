"""
Ejercicio 14

    Escribir un programa que solicita el ingreso de números primos. La lectura finalizará cuando
    ingrese un número que no sea primo. Al finalizar el programa, mostrar el factorial del número
    que tenga la mayor suma de dígitos entre todos los ingresados. Utilizar una o más funciones, 
    según sea necesario.

"""

def sumar_digitos(numero: int) -> int:
    """
    Devuelve la suma de todos los digitos de (numero).
    """
    suma = 0
    resto, division = numero%10, numero//10
    for _ in range(len(str(numero))):
        suma += resto
        resto = division%10
        division //= 10
    return suma

def calcular_factorial(numero: int) -> int:
    """
    Calcula y devuelve el factorial de (numero).
    """
    factorial = 1
    for n in range(1, numero+1):
        factorial *= n
    return factorial

def es_primo(numero: int) -> bool:
    """
    Indica si (numero) es o no un numero primo.
    """
    return len([n for n in range(1, numero+1) if numero % n == 0]) <= 2

def calcular_factorial_de_la_suma_primo_mas_alta() -> int:
    """
    Devuelve el factorial de la suma mas alta entre los digitos de
    los numeros primos que ingrese el usuario
    """
    numero = 1
    mayor_suma = 0
    while es_primo(numero):
        numero = int(input("Dame un numero primo: "))
        mayor_suma = max(mayor_suma, sumar_digitos(numero))
    return calcular_factorial(mayor_suma)

print(f"El factorial de la mayor suma de digitos es {calcular_factorial_de_la_suma_primo_mas_alta()}")