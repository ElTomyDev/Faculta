"""
Ejercicio 20

texto en negrita Escribir un programa para una empresa que tiene salas
de juegos para todas las edades y quiere calcular de forma automática 
el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe
pagar $5 y si es mayor de 18 años, $10.

"""

def calcular_entrada_segun_la_edad(edad : int):
    """
    Dada una (edad) calcula la misma y devuelve el precio a cobrar
    """
    if edad < 4:
        return "$0"
    elif edad <= 18:
        return "$5"
    else:
        return "$10"

pedir_edad = int(input("Dame una edad: "))

print(f"""
    La edad ingrasada es '{pedir_edad}' por lo tanto debe pagar {calcular_entrada_segun_la_edad(pedir_edad)} pesos.
""")