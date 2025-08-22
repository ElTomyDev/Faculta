"""
Ejercicio 15 bis

    Escribir un programa pida dos números enteros e informe por pantalla
    cual es menor de los dos, si son iguales, indicarlo por separado.

"""

def informar_sobre_numero(numero1, numero2):
    """
    Devuelve una cadena que informa si (numero1) es menor a (numero2) y biceversa
    o si son iguales.
    """
    return f"El numero {min(numero1, numero2)} es menor".upper() if numero1 != numero2 else "los numeros son iguales.".upper()

pedir_numero_uno = int(input("Dame el primer numero: "))
pedir_numero_dos = int(input("Dame el segundo numero: "))

print(f"""
    Los numeros elegidos son {pedir_numero_uno} y {pedir_numero_dos}. 
      
    Por lo tanto: {informar_sobre_numero(pedir_numero_uno, pedir_numero_dos)}
    """)