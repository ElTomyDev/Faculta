"""
Ejercicio 2

    Escribir una función que recibe un vector de strings y retorna otro con los mismos elementos del vector de entrada pero en orden inverso.

"""
import numpy as np

def invertir_vector(vector:np.array) -> np.array:
    """
    Invierte el vector (vector) y luego devuelve un nuevo vector invertido.
    """
    invertido = np.zeros(len(vector), str)
    for index, elemento in enumerate(reversed(vector)):
        invertido[index] = elemento
    return invertido

vector = np.array(["H", "o", "l", "a"])

print(f"""
      - Vector (sin invertir) = {vector}
      - Vector (invertido) = {invertir_vector(vector)}
      """)

