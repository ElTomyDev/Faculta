"""
Ejercicio 18

    Escribir un programa que pida un número entero del 1 al 7 y muestre por pantalla
    el día de la semana correspondiente. Controlar que el número se encuentre en el rango correcto,
    si no es así, informar un error. Por ejemplo, si el número es 2 el día es martes.
    
"""

def verificar_dia_segun_numero(numero):
    """
    Dado un (numero) entre un rango del 1 al 7, devuelve una cadena con
    el dia de la semana correspondiente.
    """
    if numero == 1:
        return "Lunes"
    elif numero == 2:
        return "Martes"
    elif numero == 3:
        return "Miercoles"
    elif numero == 4:
        return "Jueves"
    elif numero == 5:
        return "Viernes"
    elif numero == 6:
        return "Sabado"
    else:
        return "Domingo"


pedir_numero = int(input("Dame un numero del 1 al 7: "))

while pedir_numero > 7 or pedir_numero < 1:
    print(f"El numero {pedir_numero} no esta dentro del rango pedido")
    pedir_numero = int(input("Dame otro numero del 1 al 7: "))
    
print(f"El numero {pedir_numero} es el dia {verificar_dia_segun_numero(pedir_numero)}")