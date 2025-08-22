"""
Ejercicio 30

Escribir un programa que pida dos números enteros e informa por pantalla todos los números pares entre ellos.

"""

primer_numero = int(input("Dame el primer numero: "))
segundo_numero = int(input("Dame el sugundo numero: "))

if primer_numero < segundo_numero:
    print("".join([f"{n} " for n in range(primer_numero, segundo_numero+1) if n % 2 == 0]))