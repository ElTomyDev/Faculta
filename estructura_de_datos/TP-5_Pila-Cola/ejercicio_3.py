"""
Ejercicio 3

    Escribir una función que invierta el orden de una pila. No debe devolver una nueva pila invertida, sino invertir la pila que ingresa por parámetro.

"""
from pila import Pila

def invertirPila(pila:Pila) -> Pila:
    nuevaPila = Pila()
    for _ in range(pila.tamaño()):
        nuevaPila.apilar(pila.desapilar())
    
    for e in nuevaPila.pila:
        pila.apilar(e)
    
    return pila

print(invertirPila(Pila([1, 2, 3, 4])))
