"""
Ejercicio 5

    Escribir una operación del TDA Lista que saque el nodo que esta al inicio de la lista 
    (posición cero) y lo ponga en el final. Hacer otra que haga lo contrario, saque el nodo 
    del final y lo ponga al inicio.
    
"""

from lista import Lista

class Lista(Lista):
    def ponerPrimeroAlFinal(self):
        if self.estaVacia() == False:
            primerNodo = self.__primero.dato
            #self.__primero = self.__primero.siguiente
            nodoAux = self.__primero
            while nodoAux.siguiente != None:
                nodoAux = nodoAux.siguiente
            nodoAux.dato = primerNodo
        else:
            raise Exception("La lista esta vacia. No se puede realizar esta operacion.")

lista = Lista()
lista.agregarAlFinal(2);lista.agregarAlFinal(3);lista.agregarAlFinal(5)
print(lista)
lista.ponerPrimeroAlFinal()
print(lista)