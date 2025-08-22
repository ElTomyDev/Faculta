"""
Ejercicio 4

Modelar el TDA "Cronometro", que contiene un tiempo inicial y un tiempo final.

Se deben implementar las siguientes operaciones:

    Constructor: Queremos modelar el tiempo inicial y final con el TDA "Tiempo". Se pueden tener dos variables que se inicializaran en 
    otra operación de la interface.
    Comenzar: Debe recibir las hs,min y seg iniciales.
    Finalizar: Debe recibir las hs,min y seg finales.
    TiempoEmpleado: Devuelve una variable de tipo Tiempo con la diferencia entre el tiempo inicial y el final.

"""
from ejercicio_3 import Tiempo

class Cronometro:
    def __init__(self):
        self.__tiempoInicial = None
        self.__tiempoFinal = None
    
    def __repr__(self):
        return f"{self.__tiempoInicial} - {self.__tiempoFinal}"
    
    def comenzar(self, tiempoInicial:Tiempo) -> None:
        self.__tiempoInicial = tiempoInicial
        self.__tiempoFinal = None

    def finalizar(self, tiempoFinal:Tiempo) -> None:
        if self.__tiempoInicial is None:
            raise Exception("El cronometro no tiene tiempo inicial")
        if tiempoFinal < self.__tiempoInicial:
            raise Exception("El tiempo final es menor que el inicial")
        self.__tiempoFinal = tiempoFinal
    
    def tiempoEmpleado(self):
        if self.__tiempoInicial is None or self.__tiempoFinal is None:
            raise Exception("El cronometro debe tener tiempo Inicial y Final")
        return self.__tiempoInicial - self.__tiempoFinal

tInicial = Tiempo(15,0,0)
tFinal = Tiempo(20,0,0)

c = Cronometro()

c.comenzar(tInicial)
c.finalizar(tFinal)
print(c.tiempoEmpleado())