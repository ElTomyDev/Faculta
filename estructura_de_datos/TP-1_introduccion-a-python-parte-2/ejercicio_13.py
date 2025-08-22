"""
Ejercicio 13

Escribir un programa que pida números positivos (Debe dejar de pedir números cuando se ingrese uno negativo).
Al finalizar debe mostrar la cantidad de números cuya sumatoria de dígitos fue menor que 10. Utilizar
una o más funciones, según sea necesario.

"""

def sumar_digitos(numero: int) -> int:
    """
    Devuelve la suma de todos los digitos de (numero).
    """
    suma = 0
    resto, division = numero%10, numero//10
    for _ in range(len(str(numero))):
        suma += resto
        resto = division%10
        division //= 10
    return suma

def uno_si_es_menor_a_diez_cero_si_no(numero: int) -> int:
    """
    Devuelve 1 si (numero) es menor a 10, 0 si no.
    """
    return 1 if sumar_digitos(numero) < 10  else 0

def cantidad_de_numeros_sumados_igual_a_diez():
    """
    Retorna la cantidad resultante al sumar los digitos de 
    todos los numeros que ingrese el usuario.
    """
    numero = 0
    cantidad_suma_diez = 0
    while numero >= 0:
        numero = int(input("Dame un numero: "))
        cantidad_suma_diez += uno_si_es_menor_a_diez_cero_si_no(numero)
    return cantidad_suma_diez

print(f"La cantidad de sumas menor a 10 es {cantidad_de_numeros_sumados_igual_a_diez()}")


