"""
Ejercicio 8

    Escribir una función que realiza el cálculo de la suma de dos números enteros de muchos dígitos (los dos números tienen la misma cantidad de dígitos). 
    La función recibe dos pilas por parámetro, las que almacenan los dígitos de los números a sumar 
    (esta pilas no deben estar modificadas al terminar la función). La función debe retornar una nueva pila con el resultado.

        Por ejemplo para sumar: 85699625 + 75426652

        Las pilas de entrada a la función son:

            Pila1 = 8, 5, 6, 9, 9, 6, 2, 5

            Pila2 = 7, 5, 4, 2, 6, 6, 5, 2

        La salida:

            pilaSalida = 1, 6, 1, 1, 2, 6, 2, 7, 7

"""
from pila import Pila

def sumarPilas(pila, otraPila) -> Pila:
    suma

