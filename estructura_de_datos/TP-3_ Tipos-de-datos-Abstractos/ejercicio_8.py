"""
Ejercicio 8

    La unaHur nos pidió ayuda para administrar los edificios de laboratorios del campus. Se debe crear el TDA EdificiosLaboratorios
    con la cantidad de laboratorios disponibles, cosa que no va a cambiar.

    Cada laboratorio tiene una cantidad de computadoras, una cantidad de sillas y la cantidad de ventanas.

    Se recomienda crear primero el TDA Laboratorio.

    Implementar al menos las siguientes operaciones del TDA EdificioLaboratorios:

        definirLaboratorio(indiceLaboratorio, cantCompus, cantSillas, cantVentanas): donde el índice está entre 0 y la cantidad de laboratorios 
        que tiene el edificio. Si el laboratorio ya existía, es decir, la posicion estaba ocupada en el edificio, se tiene que redefinir (modificar).

        laboratorioConMasVentanas(): que devuelve el laboratorio con más ventanas en el edificio. Notar que no necesariamente están todos los laboratorios definidos.

        laboratoriosGrandes(nCompus): que retorna la cantidad de laboratorios en el edificio que tienen mas computadoras que la cantidad que se recibe por parámetro.

        vaciarLaboraratorios(): que elimina los laboratorios definidos

    ¡No son las únicas operaciones necesarias, agregar los métodos que crean necesarios, como el constructor!
"""
import numpy as np

def validarTipo(variable:any, nombre:str, tipo:type) -> any:
    if not isinstance(variable, tipo):
        raise Exception(f"La variable {nombre} debe ser de tipo {tipo}.")
    return variable

def validarNumeroNatural(numero:int, nombre:str) -> int:
    validarTipo(numero, nombre, int)
    if numero < 0:
        raise Exception(f"La variable {nombre} debe ser un numero natural")
    return numero

class Laboratorio:
    def __init__(self, cantCompus=0, cantSillas=0, cantVentanas=0):
        self.__cantCompus = validarNumeroNatural(cantCompus, "cantCompus")
        self.__cantSillas = validarNumeroNatural(cantSillas, "cantSillas")
        self.__cantVentanas = validarNumeroNatural(cantVentanas, "cantVentanas")
    
    def __repr__(self) -> str:
        return f"Compus: {self.__cantCompus} / Sillas: {self.__cantSillas} / Ventanas: {self.__cantVentanas}"
    
    def compus(self) -> int:
        return self.__cantCompus
    
    def sillas(self) -> int:
        return self.__cantSillas
    
    def ventanas(self) -> int:
        return self.__cantVentanas
    

class EdificioLaboratorios:
    def __init__(self):
        self.__laboratorios = np.empty(3, dtype=Laboratorio)
    
    def __repr__(self) -> str:
        return f"Cantidad de laboratorios: {len(self.__laboratorios)}"
    
    def laboratorios(self) -> np.ndarray:
        return self.__laboratorios
    
    def definirLaboratorio(self, indiceLaboratorio:int, cantCompus:int, cantSillas:int, cantVentanas:int):
        if indiceLaboratorio > len(self.__laboratorios)-1 or indiceLaboratorio < 0:
            raise Exception(f"No existe el laboratorio con indice: {indiceLaboratorio}  debe ser entre 0 y {len(self.__laboratorios)-1}")    
        self.__laboratorios[indiceLaboratorio] = Laboratorio(cantCompus, cantSillas, cantVentanas)
        
    def laboratorioConMasVentanas(self) -> Laboratorio:
        laboratorioMasVentanas = Laboratorio()
        for labo in self.__laboratorios:
            if labo != None:
                if laboratorioMasVentanas.ventanas() < labo.ventanas():
                    laboratorioMasVentanas = labo
        return laboratorioMasVentanas
    
    def laboratoriosGrandes(self, cantCompus:int) -> int:
        cantGrandes = 0
        for labo in self.__laboratorios:
            if labo != None:
                if labo.obtenerCantidadDeCompus() > cantCompus:
                    cantGrandes += 1
        return cantGrandes
    
    def vaciarLaboratorios(self):
        for idx in range(len(self.__laboratorios)):
            self.__laboratorios[idx] = None

labo1 = Laboratorio(3,4,2)
labo2 = Laboratorio(4,4,4)
labo3 = Laboratorio(2,2,1)
ed = EdificioLaboratorios()

print(ed)

ed.definirLaboratorio(0, labo1.compus(), labo1.sillas(), labo1.ventanas())
ed.definirLaboratorio(1, labo2.compus(), labo2.sillas(), labo2.ventanas())
ed.definirLaboratorio(2, labo3.compus(), labo3.sillas(), labo3.ventanas())

print(ed.laboratorioConMasVentanas().ventanas())

print(ed.laboratoriosGrandes(2))

ed.vaciarLaboratorios()
print(f"{[labo for labo in ed.laboratorios()]}")