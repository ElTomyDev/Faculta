"""
Ejercicio 11

Implementar el TDA Cola (Queue), con las siguientes operaciones:

    Crear (init())
    Vaciar
    Encolar elemento (enqueue)
    Desancolar elemento (dequeue)
    Obtener primer elemento (top)
    Obtener tamaño de cola
    Clonar
    Esta vacía.
    repr(). Para poder imprimir una Cola por consola

"""
import copy as cp

class Cola:
  def __init__(self):
    self.cola = []

  def tamaño(self)->int:
    return len(self.cola)

  def estaVacia(self)->bool:
    return self.tamaño() == 0

  def encolar(self, dato:int)->None:
    self.cola.append(dato) #Encolando por el final
    #self.cola.insert(0,dato) #Encolando por el inicio

  def tope(self)->int:
    datoCima = None
    if not self.estaVacia():
      datoCima = self.cola[0]  #Desencolo por el inicio
      #datoCima = self.cola[len(self.cola)-1] #Desencolo por el final
    return datoCima

  def desencolar(self)->int:
    dato = None
    if not self.estaVacia():
      dato = self.cola.pop(0)  #Desencolando por el inicio
      #dato = self.cola.pop() #Desencolando por el final
    return dato

  def vaciar(self)->None:
    self.cola = []

  def clonar(self):
    return cp.deepcopy(self)

  def __repr__(self)->str:
    return str(self.cola)