"""
Ejercicio 31

Escribir un programa que pida un número entero y muestre por pantalla
la cantidad de cifras de dicho número. Se debe resolver con divisiones 
sucesivas por 10 usando un bucle while.

"""
pedir_numero = int(input("Dame un numero: "))
cifras = 1
while pedir_numero > 0:
    cifras += 1 
    pedir_numero //= 10

print(f"La cantidad de cifras es: {cifras}")