"""
Ejercicio 10

Escribir una función que dado un año, retorne verdadero si es bisiesto y falso en caso contrario.

Nota: Los años bisiestos son múltiplos de 4 y no son múltiplos de 100, 
    pero los años múltiplos de 400 si son bisiestos. Estos son algunos 
    ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto,
    2000 es bisiesto, 1900 no es bisiesto

"""

def es_bisiesto(un_año: int) -> bool :
    """
    Devuelve si (un_año) es o no bisiesto
    """
    return (un_año % 4 == 0 and un_año % 100 != 0) or un_año % 400 == 0

pedir_año = int(input("Dame un año: "))

print(f"El año {pedir_año} {"es bisiesto" if es_bisiesto(pedir_año) else "no es bisiesto"}")