"""
Ejercicio 28

Escribir un programa que pida un número natural N e imprima por pantalla la suma de los números naturales de 1 hasta N.

Por ejemplo para N = 5, la salida debe ser:

1 + 2 + 3 + 4 + 5 = 15

Solo debe imprimir el resultado final (por ejemplo 15)

"""

def sumar_del_uno_hasta(numero : int):
    """
    Suma numeros desde el 1 hasta (numero) y devuelve la suma completa y el resultado
    de dicha suma
    """
    return "".join([f"{i}" if i == 1 else f" + {i}" for i in range(1, numero +1)]), str(sum([i for i in range(1, numero + 1)]))

pedir_numero = int(input("Dame un numero: "))

suma, resultado = sumar_del_uno_hasta(pedir_numero)

print(f"""
    {suma} = {resultado}
""")