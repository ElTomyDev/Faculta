"""
Ejercicio 23

    Escribir un programa que pregunte un nombre en la consola
    y un número entero e imprima por pantalla en líneas distintas
    el nombre tantas veces como el número introducido.
    
"""
pedir_nombre = str(input("Dame un nombre: "))
pedir_numero = int(input("Dame un numero: "))

for _ in range(pedir_numero):
    print(pedir_nombre)