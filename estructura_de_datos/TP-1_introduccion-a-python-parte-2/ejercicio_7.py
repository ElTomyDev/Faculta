"""
Ejercicio 7

    Escribir una función que recibe tres números enteros por parámetros,
    calcula el promedio y retorna “APROBADO” si el promedio es mayor o 
    igual a 7 o “DESAPROBADO” si es menor.

"""

def comprobar_si_aprobo(nota1:int, nota2:int, nota3:int):
    """
    Calcula el promedio y retorna si el alumno aprobo o no en forma de cadena.
    """
    return "APROBADO" if (nota1 + nota2 + nota3) / 3 >= 7 else "DESAPROBADO"

print(comprobar_si_aprobo(7,6,8))