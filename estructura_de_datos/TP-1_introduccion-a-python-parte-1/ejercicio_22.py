"""
Ejercicio 22

Escribir un programa que pida dos números enteros e imprima todos los números enteros entre ellos.

"""

pedir_numero1 = int(input("Dame el primer numero: "))
pedir_numero2 = int(input("Dame el segundo numero: "))

for i in range(pedir_numero1, pedir_numero2 + 1):
    print(i, end=" ")