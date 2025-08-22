from diccionario import Diccionario
import numpy as np


def obtenerElMaximoNumero(vector:np.array)->int:
    maximoActual = 0
    for idx in range(len(vector)):
        maximoActual = max(maximoActual, vector[idx])
    return maximoActual

def contarApariciones(vector:np.array)-> Diccionario:
    maximoNumero = obtenerElMaximoNumero(vector) # Maximo numero del vector a contar sus numeros
    
    keys = tuple(f'{i}' for i in range(maximoNumero+1)) # Crea una lista K(c) = {x ∈ N : x ≤ c}
    values = tuple(0 for _ in range(maximoNumero+1)) # Crea una lista con la misma formula de arriba
    
    dic = Diccionario(keys, values) # Creo el diccionario donde se van a contar cada numero con el patron (numero: cantidad)
    
    # Almacena y cuenta los numeros correspondientes a su clave
    for n in vector:
        dic[f'{n}'] = dic[f'{n}'] + 1
    
    # Elimina las claves que no almacenaron ningun numero, osea 'key' : 0
    for k in dic.keys():
        if dic.get(k) == 0:
            dic.remove(k)
    
    return dic

miVector = np.array([1,2,6,4,5,3,6,2,5,7,2,4])
print(contarApariciones(miVector))