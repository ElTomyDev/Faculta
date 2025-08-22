"""
Ejercicio 29

Construir un programa que lea un número natural N y calcule la suma de los primeros N números pares.

    Si N = 2 -> Resultado = 2 + 4
    Si N = 3 -> Resultado = 2 + 4 + 6
    Si N = 4 -> Resultado = 2 + 4 + 6 + 8
    ......
    Para cualquier N -> Resultado = 2 + 4 + 6 +....+ 2*N

"""

pedir_numero = int(input("Dame un numero: "))

for n in range(1, pedir_numero+1):
    ecuacion = "".join([f"{i*2}" if i == 1 else f" + {i*2}" for i in range(1,n)])
    resultado = ecuacion.split(" + ")
    suma = sum([int(i) for i in resultado if i != ''])
    if suma != 0:
        print(f"{ecuacion} = {suma}")