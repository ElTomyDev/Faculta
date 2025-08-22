"""
Ejercicio 9

    Escribir un programa que pregunte un nombre completo en la consola y después muestre
    por pantalla ese nombre tres veces, una con todas las letras minúsculas, 
    otra con todas las letras mayúsculas y otra solo con la primera letra del nombre
    y de los apellidos en mayúscula. Se puede introducir un nombre combinando 
    mayúsculas y minúsculas como se quiera.
    
"""

def capitalizar_nombre_completo(nombre : str):
    """
    Dado un (nombre) devuelve el mismo pero con las primeras letras del nombre y apellido en mayusculas
    """
    nueva_cadena = ""
    for palabra in nombre.split():
        nueva_cadena += palabra.capitalize() + " "
    
    return nueva_cadena

pedir_nombre = str(input("Dame tu nombre: "))

print(f""" 
      -- Nombre ingresado: {pedir_nombre} --
      
      - Upper: {pedir_nombre.upper()}
      - Lower: {pedir_nombre.lower()}
      - Capitalize: {capitalizar_nombre_completo(pedir_nombre)}
      """)