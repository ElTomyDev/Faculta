"""
Ejercicio 3

    Escribir la función sumaDeVectores que recibe dos vectores de enteros del mismo tamaño 
    y retorna otro con la suma de ambos. La suma de vectores se realiza componente a componente, 
    segun la siguiente forma:

        v1 = [ v11 , v12 , v13 , ... , v1N ]

        v2 = [ v21 , v22 , v23 , ... , v2N ]

        v1 + v2 = [ v11 + v21 , v12 + v22 , v13 + v23 , ... , v1N + v2N ]

"""
import numpy as np

def suma_de_vectores(vector1: np.array, vector2: np.array) -> np.array:
    """
    Retorna un vector con la suma de cada elemento de (vector1) y (vector2)
    respetando sus pociciones. Si no puede, lanza un mensaje de error. 
    """
    if len(vector1) == len(vector2):
        vector_sumas = np.zeros(len(vector1), int)
        for index in range(len(vector_sumas)):
            # print(type(vector1[index]))
            if (type(vector1[index]) == np.int64) and (type(vector2[index]) == np.int64):
                vector_sumas[index] = vector1[index] + vector2[index]
            else:
                return """ - ERROR -
                Los vectores deben ser SOLO numeros enteros.
                """
        return vector_sumas
    else:
        return """ - ERROR -
                Los vectores deben ser del mismo tamaño.
            """
mi_vector1 = np.array([2, 4, 5, 6])
mi_vector2 = np.array([2, 4, 5, 6])

print(f"""
    Los vectores ingresados son {mi_vector1} y {mi_vector2}
    Vector sumado : {suma_de_vectores(mi_vector1, mi_vector2)}
""")