"""

Ejercicio 2

Implementar el TDA "Cuenta" que modela una cuenta bancaria, la estructura de datos esta compuesta por los siguientes componentes:

    Número de cuenta
    DNI del titular
    Saldo de cuenta actual
    Interés anual

Implementar las siguientes operaciones:

    Constructor: Debe incluir las validaciones necesarias.
    __repr__: Al usar la función print con una variable del tipo cuenta debe mostrar: Cuenta Nro: 'numero' - Titular: 'dni' ($'saldo').
    actualizarSaldo: Operación que actualiza el saldo de la cuenta aplicándole el interés diario (interés anual dividido entre 365).
    ingresarDinero: Operación que recibe un número e ingresa esa cantidad en la cuenta.
    retirarDinero: Operación que recibe un número y extrae esa cantidad de la cuenta (si hay saldo disponible), sino debe lanzar una excepción.

"""
def validarTipo(variable:any, nombre:str, tipo:type) -> any:
    if not isinstance(variable, tipo):
        raise Exception(f"La variable {nombre} debe ser de tipo {tipo}.")
    return variable

def validarNumero(variable:any, nombre:str) -> int:
    validarTipo(variable, nombre, int)
    if variable < 0:
        raise Exception(f"La variable {nombre} debe ser mayor o igual a 0")
    return variable

class Cuenta:
    def __init__(self, numero_cuenta:int, dni:int, interes:int):
        self.__numero_cuenta = validarNumero(numero_cuenta, "numero_cuenta")
        self.__dni = validarNumero(dni, "dni")
        self.__interes = validarNumero(interes, "interes")
        self.__saldo = 0
    
    def __repr__(self) -> str:
        return f" Cuenta Nro: {self._numero_cuenta} - Titular: {self._dni} (${self._saldo:.2f})"
    
    def actualizar_saldo(self) -> None:
        self._saldo = self._saldo - (self._interes / 365)
    
    def ingresar_dinero(self, cnatidad:int) -> None:
        self._saldo += cnatidad
    
    def retirar_dinero(self, cantidad) -> None:
        if self._saldo < cantidad:
            raise Exception(f"No tienes saldo suficiente")
        self._saldo -= cantidad

mi_cuenta = Cuenta(2233, 46265023, 2000)

print(mi_cuenta)

mi_cuenta.actualizar_saldo() 
print(mi_cuenta) 
        
mi_cuenta.ingresar_dinero(40000)
print(mi_cuenta) 

mi_cuenta.retirar_dinero(20000)
print(mi_cuenta)
