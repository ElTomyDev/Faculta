"""
Ejercicio 1

Implementar el TDA "Propiedad" que modela un inmueble, con una estructura definida por los siguientes componentes:

    Calle
    Número
    Localidad
    Año de construcción
    Cantidad de ambientes

Implementar las siguientes operaciones:

    Constructor: Debe incluir las validaciones necesarias, teniendo en cuenta que solo se almacenan propiedades construidas luego de 1870.
    __repr__: Al usar la función print con una variable del tipo propiedad debe mostrar: 'calle' 'numero' ('localidad').
    mismaLocalidad: Operación que recibe dos propiedades y retorna True si estan en la misma localidad y False en caso contrario.
    mismaCalle: Operación que recibe dos propiedades y retorna True si estan en la misma calle y False en caso contrario.
    mayorNumeración: Operación que recibe dos propiedades y si están en la misma calle de la misma localidad, retorna la propiedad que posee mayor numeración. Si están calles o en localidades diferentes debe lanzar una excepción.
    calculaImpuestoARBA: Operación que retorna el porcentaje de impuesto inmobiliario de una propiedad, según la siguiente regla:
        Propiedades entre 1871 y 1949:
            Entre 1 y 3 ambientes: 5% de impuesto
            Entre 4 y 6 ambientes: 10% de impuesto
            Más de 6 ambientes: 25 % de impuesto
        Propiedades desde 1950 hasta la actualidad:
            Entre 1 y 5 ambientes: 5% de impuesto
            Más de 5 ambientes: 35 % de impuesto
 
"""
def validarTipo(variable:any, nombre:str, tipo:type) -> any:
    if not isinstance(variable, tipo):
        raise Exception(f"La variable {nombre} debe ser de tipo {tipo}.")
    return variable

def validarNumeroNatural(numero:int, nombre:str) -> int:
    validarTipo(numero, nombre, int)
    if numero < 0:
        raise Exception(f"La variable {nombre} debe ser un numero natural")
    return numero

def validarAmbientes(numero:int, nombre:str) -> int:
    validarTipo(numero, nombre, int)
    if numero < 1:
        raise Exception(f"La variable {nombre} debe ser un numero mayor o igual a 1")
    return numero

def validarAño(variable:any, nombre:str) -> any:
    validarTipo(variable, nombre, int)
    if variable <= 1870:
        raise Exception(f"El año de construccion debe ser mayor a 1870")
    return variable

class Propiedad:
    def __init__(self, calle:str, numero:int, localidad:str, añoDeConstruccion:int, cantidadDeAmbientes:int):
        self.__calle = validarTipo(calle, "calle", str)
        self.__numero = validarNumeroNatural(numero, "numero")
        self.__localidad = validarTipo(localidad, "localidad", str)
        self.__añoDeConstruccion = validarAño(añoDeConstruccion, "añoDeConstruccion")
        self.__cantidadDeAmbientes = validarAmbientes(cantidadDeAmbientes, "cantidadDeAmbientes")
    
    def __repr__(self):
        return f"{self.__calle} {self.__numero} ({self.__localidad})"
    
    def localidad(self) -> str:
        return self.__localidad
    
    def calle(self) -> str:
        return self.__calle
    
    def numero(self) -> int:
        return self.__numero
    
    def mismaLocalidad(propiedad:object, otra_propiedad:object) -> bool:
        return propiedad.localidad().lower() == otra_propiedad.localidad().lower()
    
    def mismaCalle(propiedad:object, otra_propiedad:object) -> bool:
        return propiedad.calle().lower() == otra_propiedad.calle().lower()
    
    def mayorNumeracion(propiedad:object, otra_propiedad:object) -> object:
        if not Propiedad.mismaCalle(propiedad, otra_propiedad) or not Propiedad.mismaLocalidad(propiedad, otra_propiedad):
            raise Exception(f"las propiedades deben estar en la misma localidad y en la misma calle")
        return propiedad if propiedad.numero() > otra_propiedad.numero() else otra_propiedad
    
    def calcularImpuestoARBA(self) -> int:
        if self.__añoDeConstruccion >= 1950:
            return 35 if self.__cantidadDeAmbientes > 5 else 5
        else:
            if self.__cantidadDeAmbientes > 6:
                return 25
            else:
                return 5 if self.__cantidadDeAmbientes <= 3 else 10
                

propiedad1 = Propiedad("Shumman", 2300, "Hurlingham", 1949, 2)
propiedad2 = Propiedad("Shumman", 2450, "Hurlingham", 2255, 6)
propiedad3 = Propiedad("Picusal", 2000, "Moron", 2255, 6)
print(Propiedad.mismaLocalidad(propiedad1, propiedad2))
print(Propiedad.mismaCalle(propiedad1, propiedad2))
print(Propiedad.mayorNumeracion(propiedad1, propiedad2))
print(f"{propiedad1.calcularImpuestoARBA()}% de impuestos ARBA")