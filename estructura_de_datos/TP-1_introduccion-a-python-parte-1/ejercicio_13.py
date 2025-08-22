"""
Ejercicio 13

    Escribir un programa que pida una palabra y un número N y muestre por pantalla la palabra ingresada repetida N veces.
    
"""

def repetir_palabra(palabra, veces):
    """
    Devuelve la misma (palabra) una determinada cantidad de (veces)
    """
    return "".join(["\n- " + palabra for _ in range(veces)])

pedir_palabra = str(input("Dame una palabra: "))
pedir_numero = int(input("Dame la cantidad de veces a repetir: "))

print(f"""
< LA PALABRA ELEGIDA ES '{pedir_palabra.upper()}' Y SE VA A REPETIR {pedir_numero} VECES >
    {repetir_palabra(pedir_palabra, pedir_numero)}
""")