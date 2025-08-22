"""
Ejercicio 7

    Escribir un función que duplique el contenido de una pila.

    Por ejemplo, si la pila de entrada es:

        Pila = 8, 5, 6, 9

    Luego de la función la salida debe ser:

        pilaSalida = 8, 5, 6, 9, 8, 5, 6, 9

"""
from pila import Pila

def invertirPila(pila:Pila) -> Pila:
    nuevaPila = Pila()
    pilaAux = pila.clonar()
    
    for _ in range(pilaAux.tamaño()):
        nuevaPila.apilar(pilaAux.desapilar())
    return nuevaPila

def duplicarPila(pila:Pila) -> Pila:
    pilaAux = invertirPila(pila)
    pilaNueva = Pila()
    for _ in range(2):
        for _ in range(pila.tamaño()):
            pilaNueva.apilar(pilaAux.tope())
            pilaAux.desapilar()
        pilaAux = invertirPila(pila)
    return pilaNueva

print(duplicarPila(Pila([2,3,4])))

