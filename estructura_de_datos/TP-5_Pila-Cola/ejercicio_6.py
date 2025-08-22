"""
Ejercicio 6

    Escribir una función que elimine de una pila todas las ocurrencias de un elemento dado. Usar una pila auxiliar.

"""
from pila import Pila
def invertirPila(pila:Pila) -> Pila:
    nuevaPila = Pila()
    pilaAux = pila.clonar()
    
    for _ in range(pilaAux.tamaño()):
        nuevaPila.apilar(pilaAux.desapilar())
    return nuevaPila

def eliminarElementos(elemento:any, pila:Pila) -> Pila:
    pilaAux = Pila()
    
    for _ in range(pila.tamaño()):
        if pila.tope() != elemento:
            pilaAux.apilar(pila.tope())
        pila.desapilar()
    
    return invertirPila(pilaAux)

print(eliminarElementos(3,Pila([3,4,5,6,3,2,4,5,3,3])))