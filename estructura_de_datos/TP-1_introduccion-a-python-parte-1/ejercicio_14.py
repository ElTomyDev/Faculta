"""
Ejercicio 14

    Escribir un programa que pregunte una edad y muestre por pantalla si es mayor de edad o no.
    
"""

def definir_edad(edad):
    """
    Devuelve si es mayor de edad o no segun una (edad) dada.
    """
    return "es mayor" if int(edad) >= 18 else "es menor"

pedir_edad = str(input("Dame la edad de Juan: "))

print(f"La edad de Juan es: {pedir_edad}, por lo tanto {definir_edad(pedir_edad)}.")