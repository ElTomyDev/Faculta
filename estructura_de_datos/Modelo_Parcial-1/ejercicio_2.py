"""
Ejercicio 2
    Una conocida empresa de venta por internet se comenzó a preocupar por los trabajadores y decidió
    elaborar un software para controlar el tamaño de las pilas de paquetes que los motoqueros llevan 
    en los envíos. Vamos a suponer que cada motoquero lleva solo una pila de paquetes en cada envío. 
    Para eso nos contrata y nos pide que modelemos el TDA EnvioEnMoto con las siguientes operaciones:

        init(pesoMaximo:float, cantidadPaquetesMaxima:int): Construye una variable de tipo EnvioEnMoto
        recibiendo el peso total máximo (en kg) y la cantidad máxima de paquetes que el motoquero puede llevar en su pila de paquetes.

        cargarPaquete(self:EnvioEnMoto, destinoPaquete:str, pesoPaquete:float)->None: Recibe los datos de un paquete y lo pone en el 
        envío, siempre que se pueda, es decir, que el envío no se pase de la cantidad de paquetes ni del peso total. Los paquetes 
        que van al mismo destino deben ir juntos en la pila. Si el paquete NO puede ser almacenado se debe lanzar una excepción.

        primerDestino(self:EnvioEnMoto)->str: Retorna el destino del paquete más pesado del envío, así el motoquero sabe a donde
        le conviene ir primero. La operación no debe modificar la pila de paquetes.

        paquetesJuntos(self:EnvioEnMoto, destino:str)->int: Recibe un destino y retorna la cantidad de paquetes que el motoquero 
        tiene que llevar allí. La operación no debe modificar la pila de paquetes.

    Notas:

        - Se recomienda primero generar el TDA Paquete.
        - Se pueden agregar todas las funciones auxiliares y/o operaciones de los TDAs que consideren necesarias además de las pedidas.
        - NO se puede usar el TDA Lista en la solución.
        - Se pueden usar todas las operaciones del TDA Pila que vimos en clase.

"""
from pila import Pila

def validarTipo(variable:any, nombre:str, tipo:type) -> any:
    if not isinstance(variable, tipo):
        raise Exception(f"La variable {nombre} debe ser de tipo {tipo}.")
    return variable

def validarNumeroPositivo(numero:any, nombre:str) -> any:
    validarTipo(numero, nombre, int)
    if numero < 0:
        raise Exception(f"{nombre} debe ser un numero mayor a 0")
    return numero

class Paquete:
    def __init__(self, peso:float, destino:str):
        self.__peso = validarNumeroPositivo(peso, "Peso")
        self.__destino = destino
    
    def getPeso(self) -> float:
        return self.__peso
    
    def getDestino(self) -> str:
        return self.__destino

class EnvioEnMoto:
    def __init__(self, pesoMaximo:float, cantidadMaxima:int):
        self.__pesoMaximo = validarNumeroPositivo(pesoMaximo, "PesoMaximo")
        self.__cantidadMaxima = validarNumeroPositivo(cantidadMaxima, "CantidadMaxima")
        self.__pesoTotalActual = 0
        self.__paquetes = Pila()
    
    def pesoLlegoAlLimite(self) -> bool:
        return self.__pesoTotalActual >= self.__pesoMaximo
    
    def entranPaquetes(self):
        return self.__paquetes.tamaño() < self.__cantidadMaxima
    
    def cargarPaquete(self, destino:str, peso:float) -> None:
        if self.pesoLlegoAlLimite():
            raise Exception(f"El peso llego al limite")
        if not self.entranPaquetes():
            raise Exception("Ya no entran mas paquetes")
        
        if not self.__paquetes.estaVacia():
            for _ in range(self.__paquetes.tamaño() - 1):
                if self.__paquetes.tope().getDestino().lower() == destino.lower():
                    self.cargarPaqueteConDestinosIguales(destino, peso)
                    break
                else:
                    self.__paquetes.desapilar()
        else:
            self.__paquetes.apilar(Paquete(peso, destino))
        self.__pesoTotalActual += peso
    
    def cargarPaqueteConDestinosIguales(self, destino:str, peso:float) -> None:
        pila_aux = Pila()
        for _ in range(self.__paquetes.tamaño() - 1):
                if self.__paquetes.tope().getDestino().lower() == destino:
                        self.__paquetes.apilar()
                        
                
