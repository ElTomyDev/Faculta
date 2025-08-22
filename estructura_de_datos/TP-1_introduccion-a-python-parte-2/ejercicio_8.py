"""
Ejercicio 8

    Escribir una función que recibe dos números enteros mayores que 1,
    n y m, y retorna la potencia n a la m. Resolver con una estructura
    de control repetitiva, NO con el operador potencia de Python

"""

def potencia_de_n_y_m(numero1, numero2):
    """
    Recibe dos numeros y retorna la potencia de los 2.
    """
    potencia = 1
    for n in range(numero2):
        potencia *= numero1
    return potencia if numero1 > 1 and numero2 > 1 else "Los numeros deben ser mayor o igual a 1"

print(potencia_de_n_y_m(2,3))