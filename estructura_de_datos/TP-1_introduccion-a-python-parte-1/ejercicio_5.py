"""
Ejercicio 5

    Escribir un programa que pida una temperatura en grados Celsius al usuario, realice la transformación
    de grados Celsius a Fahrenheit e imprima el resultado por pantalla.
    
"""

def convertir_a_fahrenheit(grados_celsius):
    """
    Convierte y devuelve los grados Celsius (grados_celsius) a grados Fahrenheit.
    """
    return 1.8*grados_celsius + 32

pedir_grados_celsius = int(input("Ingrese la temperatura en Celsius: "))

grados_fahrenheit = int(convertir_a_fahrenheit(pedir_grados_celsius))

print(f"""
      Ingreso {pedir_grados_celsius} grados Celsius, que son {grados_fahrenheit} en grados Fahrenheit.
      """)