"""
Ejercicio 11

    Escribir un programa que pida una palabra, reemplace todas las letras "a" por "z" y muestre el resultado por pantalla.
    
"""

def reemplazar_letras_a_por_z(palabra : str):
    """
    Dada una (palabra), reemplaza todas las letras 'a' por la letra 'z' y despues
    devuelve la nueva palabra con las letras reemplazadas.
    """
    return palabra.replace("a", "z")

pedir_palabra = str(input("Dame una palabra: "))

print(f"""
      - La palabra usada es: {pedir_palabra.upper()}
      - La palabra reemplazada es: {reemplazar_letras_a_por_z(pedir_palabra).upper()}
      """)