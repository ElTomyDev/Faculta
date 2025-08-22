"""
Ejercicio 11

Escribir un programa que pida dos años y escriba cuántos años bisiestos
hay entre esas dos fechas (incluidos los dos años).

"""

def es_bisiesto(un_año: int) -> bool :
    """
    Devuelve si (un_año) es o no bisiesto
    """
    return (un_año % 4 == 0 and un_año % 100 != 0) or un_año % 400 == 0

def cantidad_de_años_biciestos(año1: int, año2: int) -> int:
    """
    Devuelve la cantidad de años biciestos que hay entre (año1) y (año2).1
    """
    lista_años = [año for año in range(año1, año2+1) if es_bisiesto(año)]
    print(lista_años)
    return len(lista_años)

año1 = int(input("Dame el primer año: "))
año2 = int(input("Dame el segundo año: "))

print(f"La cantidad de años bisiestos entre {año1} y {año2} es {cantidad_de_años_biciestos(año1, año2)}")