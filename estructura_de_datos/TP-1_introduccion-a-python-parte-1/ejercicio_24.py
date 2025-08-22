"""
Ejercicio 24

    Escribir un programa que pida un número entero positivo y muestre por pantalla
    todos los números impares desde 1 hasta ese número.

"""

pedir_numero = int(input("Dame un numero: "))

if pedir_numero > 0:
    for n in range(1, pedir_numero + 1):
        if n % 2 != 0:
            print(n, end=" ")
else:
    print("El numero tiene que ser un entero positivo")