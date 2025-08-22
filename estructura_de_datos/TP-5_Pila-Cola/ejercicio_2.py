"""
Ejercicio 2

    Escribir un programa que declare una pila de enteros y le apile 4 elementos. Luego debe mostrar la pila y su tamaño,
    desapilar 2 elementos y volver a imprimirla junto con el nuevo tamaño

"""
from pila import Pila

def pilaDeEnteros() -> Pila:
    miPila = Pila()
    
    miPila.apilar(2)
    miPila.apilar(3)
    miPila.apilar(4)
    miPila.apilar(5)
    
    print(f"Pila = {miPila} - Tamaño: {miPila.tamaño()}")
    
    miPila.desapilar()
    miPila.desapilar()
    
    print(f"Pila = {miPila} - Tamaño: {miPila.tamaño()}")

pilaDeEnteros()