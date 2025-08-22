"""
Ejercicio 21

Mostrar por pantalla todos los números enteros entre 1 y 100, 
hacerlo usando un bucle while y tambien con un bucle for.

"""
numero = 1

while numero <= 100:
    print(numero, end=" ")
    numero += 1

print("\n")

for i in range(1, numero): # Al saber que (numero) termina en 100 lo utilizo en el for
    print(i, end=" ")
