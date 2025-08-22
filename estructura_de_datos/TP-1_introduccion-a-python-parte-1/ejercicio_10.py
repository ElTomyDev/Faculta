"""
Ejercicio 10

    Escribir un programa que pregunte un nombre en la consola y después muestre por pantalla: 
    "El <NOMBRE> tiene <N> letras", donde <NOMBRE> es el nombre ingresado todo en mayúsculas 
    y <N> es el número de letras que tienen el nombre.
    
"""

pedir_nombre = str(input("Dame un nombre: "))

print(f"El nombre {pedir_nombre.capitalize()} tiene {len(pedir_nombre)} letras.")