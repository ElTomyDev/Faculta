"""
Ejercicio 4

    Escribir una función que toma el último elemento de una pila(la base) y lo ponga en la 
    cima (de la misma pila), respetando el orden del resto de los elementos. Utilizar una pila auxiliar.

"""
from pila import Pila

def invertirPila(pila:Pila) -> Pila:
    nuevaPila = Pila()
    pilaAux = pila.clonar()
    
    for _ in range(pilaAux.tamaño()):
        nuevaPila.apilar(pilaAux.desapilar())
    
    return nuevaPila

def apilarUltimoElemento(pila:Pila) -> Pila:
    pilaAux = invertirPila(pila)
    pila.apilar(pilaAux.tope())
    return pila

print(apilarUltimoElemento(Pila([1, 2, 3, 4])))
    