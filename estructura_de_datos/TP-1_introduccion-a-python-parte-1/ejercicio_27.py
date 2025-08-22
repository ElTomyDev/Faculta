"""
Ejercicio 27

Escribir un programa que pida un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

Si el usuario ingresa el numero 5:

1

3 1

5 3 1

7 5 3 1

9 7 5 3 1 
"""

pedir_numero = int(input("Dame un numero: "))

for n in range(1, pedir_numero+1, 2):
    print("".join([f"{i} " for i in range(n, 0, -2)]))
        