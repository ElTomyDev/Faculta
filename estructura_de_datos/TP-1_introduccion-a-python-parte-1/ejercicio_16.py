"""
Ejercicio 16

    Escribir un programa que pida un número entero e indique si dicho número es par o impar.
    
"""

def verificar_par_o_impar(numero):
    """
    Devuelve una cadena si el (numero) dado es par o impar.
    """
    return "ES PAR" if numero % 2 == 0 else "ES IMPAR"

pedir_numero = int(input("Dame un numero: "))

print(f"El numero {pedir_numero} {verificar_par_o_impar(pedir_numero)}")