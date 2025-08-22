"""
Ejercicio 32

Escribir un programa que pida un número entero e informe si dicho numero es primo o compuesto.

"""

pedir_numero = int(input("Dame un numero: "))

lista = [n for n in range(1, pedir_numero+1) if pedir_numero % n == 0]

if len(lista) <= 2:
    print(f"{pedir_numero} ES PRIMO")
else:
    print(f"{pedir_numero} ES COMPUESTO")        