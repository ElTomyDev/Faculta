"""
Ejercicio 12

    Escribir una función que tome por parámetro un numero entero y retorne la suma de sus dígitos.
    Para obtener los digitos deben ir dividiendo (division entera) por 10 sucesivamente y tomando
    el resto (digito que esta mas a la derecha).

"""

def sumar_digitos(numero: int) -> int:
    """
    Devuelve la suma de todos los digitos de (numero).
    """
    suma = 0
    resto, division = numero%10, numero//10
    for _ in range(len(str(numero))):
        suma += resto
        resto = division%10
        division //= 10
    return suma

pedir_numero = int(input("Dame un numero: "))

print(f"La suma de los digitos de {pedir_numero} es {sumar_digitos(pedir_numero)}")
