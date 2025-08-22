"""
Ejercicio 1

Implementar el TDA Pila (Stack), con las siguientes operaciones:

    - Crear (init())
    - Vaciar
    - Apilar elemento (push)
    - Desapilar elemento (pop)
    - Obtener primer elemento (top)
    - Obtener tamaño de pila
    - Clonar
    - Esta vacía.
    - repr(). Para poder imprimir una Pila por consola

"""
import copy as cp

class Pila:
    def __init__(self, listaInicial:list=[]):
        self.pila = []
        if listaInicial:
            self.pila = cp.deepcopy(listaInicial)
            
    def tamaño(self)->int:
        return len(self.pila)

    def estaVacia(self)->bool:
        return self.tamaño() == 0

    def apilar(self, dato:int)->None:
        self.pila.append(dato)

    def tope(self)->int:
        datoCima = None
        if not self.estaVacia():
            datoCima = self.pila[len(self.pila)-1] # leo ultimo elemento
        return datoCima
    
    def desapilar(self) -> int:
        dato = None
        if not self.estaVacia():
            dato = self.pila.pop()
            return dato
    
    def vaciar(self) -> None:
        self.pila = []
    
    def clonar(self):
        return cp.deepcopy(self)
    
    def __repr__(self):
        return str(self.pila)