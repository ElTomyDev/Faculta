"""
Ejercicio 6

Escribir una función que calcule el área de un círculo
y otra que calcule el volumen de un cilindro usando la primera función.

"""

def calcular_area_de_circulo(radio : float):
    """
    Calcula y devuelve el area de un circulo.
    """
    return 3.14 * (radio**2)

def calcular_volumen_de_cilindro(radio:float, altura:float):
    """
    Calcula y devuelve el volumen de un cilindro.
    """
    return calcular_area_de_circulo() * altura