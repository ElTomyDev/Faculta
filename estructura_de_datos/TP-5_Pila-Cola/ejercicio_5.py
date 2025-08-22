"""
Ejercicio 5

    Escribir una función que coloque en el fondo de una pila un nuevo elemento.

"""
from pila import Pila

def invertirPila(pila:Pila) -> Pila:
    nuevaPila = Pila()
    pilaAux = pila.clonar()
    
    for _ in range(pilaAux.tamaño()):
        nuevaPila.apilar(pilaAux.desapilar())
    return nuevaPila

def colocarElementoAlFondo(elemento:any, pila:Pila) -> Pila:
    pilaAux = Pila([elemento])
    pila = invertirPila(pila)
    
    for _ in range(pila.tamaño()):
        pilaAux.apilar(pila.desapilar())
    return pilaAux

print(colocarElementoAlFondo(1, Pila([2,3,4])))