"""
Ejercicio 1

    Escribir una función que recibe un numero entero N y le pide al usuario que ingrese N numeros. 
    Al final, el programa debe retornar un vector contiendo los números que fueron ingresados. Tambien debe
    imprimir por pantalla la suma total de los valores y el promedio. Se deben hacer funciones para resolver el promedio y la suma total.
    
"""

import numpy as np

def obtener_numeros_por_usuario(n: int) -> np.array:
    """
    Retorna un vector con todos los numeros que ingreso el usuario.
    La cantidad de numeros a ingresar es (n).
    """
    contador = 0
    vector = np.zeros(n, int)
    while contador < n:
        pedir_numero = int(input("Dame un numero: "))
        vector[contador] = pedir_numero
        contador += 1
    
    return vector

def suma_total(vector: np.array) -> int:
    """
    Retorna la suma de todos los enteros que tiene (vector)
    """
    suma = 0
    for num in vector:
        suma += num
    return suma

def promedio(vector:np.array) -> float:
    return suma_total(vector) / len(vector)

numeros = obtener_numeros_por_usuario(5)

print(f"""
        - Numeros ingresados: {numeros}
        - Suma Total: {suma_total(numeros)}
        - Promedio: {promedio(numeros)}
      """)
