"""
Ejercicio 3

Implementar el TDA "Tiempo" que modela una duracion en horas, minutos y segundos.

Se deben implementar las siguientes operaciones:

    Constructor: Debe incluir las validaciones necesarias, la hora debe ser un número positivo y los minutos y segundos deben ser números positivos entre 0 y 59.
    __repr__: Al usar la función print con una variable del tipo tiempo debe mostrar: 'horas':'minutos':'segundos'.
    tiempoASegundos: Operación que toma una variable de tipo tiempo y retorna la cantidad en segundos.
    tiemposDesdeSegundos: Operación que recibe un tiempo en segundos como parámetro y retorna una variable de tipo tiempo, en horas minutos y segundos.
    mayorDuracion: Operación que recibe dos variables de tipo tiempo y retorna la de mayor duración.

"""

def validarTipo(variable:any, nombre:str, tipo:type) -> any:
    if not isinstance(variable, tipo):
        raise Exception(f"La variable {nombre} debe ser de tipo {tipo}.")
    return variable

def validarNumeroNatural(variable:int, nombre:str) -> int:
    print(variable)
    validarTipo(variable, nombre, int)
    if variable < 0:
        raise Exception(f"La variable {nombre} debe ser mayor o igual a 0")
    return variable

def validarTiempo(variable:int, nombre:str) -> int:
    validarNumeroNatural(variable, nombre)
    if variable < 0:
        raise Exception(f"{nombre} no puede ser menor a 0")
    elif variable > 59:
        raise Exception(f"{nombre} no puede ser mayor a 60")
    return variable

class Tiempo:
    def __init__(self, horas:int, minutos:int, segundos:int):
        self.__horas = validarNumeroNatural(horas, "horas")
        self.__minutos = validarTiempo(minutos, "minutos")
        self.__segundos = validarTiempo(segundos, "segundos")
    
    def __repr__(self) -> str:
        return f"{self.__horas}:{self.__minutos}:{self.__segundos}"
    
    def horas(self):
        return self.__horas
    
    def minutos(self):
        return self.__minutos
    
    def segundos(self):
        return self.__segundos
    
    def tiempoASegundos(tiempo) -> int:
        return (((tiempo.__horas * 60) + tiempo.__minutos) * 60) + tiempo.__segundos
    
    def tiempoDesdeSegundos(segundos:int):
        horas = segundos // 3600
        segundos %= 3600
        minutos = segundos // 60
        segundos %= 60
        
        return Tiempo(horas, minutos, segundos)
    
    def mayorDuracion(tiempo, otroTiempo):
        return tiempo if (Tiempo.tiempoASegundos(tiempo) > Tiempo.tiempoASegundos(otroTiempo)) else otroTiempo
    
    def __sub__(tiempo1:object, tiempo2:object) -> object:
        return Tiempo.tiempoDesdeSegundos(tiempo1.tiempoASegundos() - tiempo2.tiempoASegundos())
    
    def __le__(tiempo1:object, tiempo2:object) -> bool:
        return tiempo1.tiempoASegundos() <= tiempo2.tiempoASegundos()
    
    def __lt__(tiempo1:object, tiempo2:object) -> bool:
        return tiempo1.tiempoASegundos() < tiempo2.tiempoASegundos()
    
    def __eq__(tiempo1:object, tiempo2:object) -> bool:
        return tiempo1.tiempoASegundos() == tiempo2.tiempoASegundos()
    
    def __gt__(tiempo1:object, tiempo2:object) -> bool:
        return tiempo1.tiempoASegundos() > tiempo2.tiempoASegundos()
    
    def __ge__(tiempo1:object, tiempo2:object) -> bool:
        return tiempo1.tiempoASegundos() >= tiempo2.tiempoASegundos()

mi_tiempo = Tiempo(24,34,0)
otro_tiempo = Tiempo(66,32,0)
print(mi_tiempo)
print(otro_tiempo)

print(Tiempo.tiempoASegundos(mi_tiempo))
print(Tiempo.tiempoDesdeSegundos(4009520950239052950926))
        
        