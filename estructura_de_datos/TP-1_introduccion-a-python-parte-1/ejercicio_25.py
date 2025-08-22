"""
Ejercicio 25

Escribir un programa que pida un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, de altura 
igual al número introducido.

Por ejemplo, si el usuario ingresa el numero 4:
    *
    * *
    * * *
    * * * *
"""

pedir_numero = int(input("Dame un numero: "))

for n in range(1, pedir_numero+1):
    print(f"{"".join(["* " for i in range(n)])}")