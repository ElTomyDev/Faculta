"""
Ejercicio 15

    Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable 
    y luego pregunte por la contraseña e imprima por pantalla si la contraseña introducida 
    en la consola coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
    
"""

CONTRASEÑA = "HoLa123"

def validar_contraseña(contraseña_pedida):
    """
    Devuelve si la contraseña es o no correcta segun una (contraseña_pedida)
    """
    return "La contraseña es correcta" if contraseña_pedida.lower() == CONTRASEÑA.lower() else "Contraseña incorrecta"

pedir_contraseña = str(input("Ingrese la contraseña: "))

print(validar_contraseña(pedir_contraseña))