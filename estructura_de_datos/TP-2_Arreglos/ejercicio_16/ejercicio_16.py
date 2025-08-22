"""
Ejercicio 16

Una de las aplicaciones de matrices en programación es la representación y procesamiento de imágenes. Vamos a ver algunas cosas que se pueden hacer. 
Para esto primero tenemos que cargarnos una imagen en el colab y generar una matriz a partir de ella.

    Descarguen el archivo "felix.csv" del siguiente link: https://drive.google.com/file/d/10Du9ECx7Cz-aHXQpYaWjkaAn6wKJSArn/view?usp=sharing
    Suban el archivo "felix.csv" al "colab" para poder cargarlo con el programa de Python de abajo (haciendo click en el icono de la carpeta texto alternativo, 
    de arriba a la izquierda y luego en "Subir")
    Completen el programa, procesando a la imagen guardada en la matriz "felix" para obtener las imágenes
    de la siguiente figura (La "A" es la imagen original), pueden hacer funciones que generen cada transformación en la imagen:
    
        (No se puede poner la imagen por motivos que deven esta claros xd)
"""
import numpy as np
import matplotlib.pyplot as plt
import copy as cp
import pandas as pd
import os


def read_csv_and_return(path:str) -> np.ndarray:
    """
    Se encarga de leer el archivo csv que esta en (path)
    y luego lo retorna en una matriz.
    """
    if os.path.exists(path):
        return np.genfromtxt(path, delimiter=",")
    else:
        raise Exception(f"Error: no se a encontrado la ruta {path}. Porfavor asegurate de que la ruta sea correcta.")

def show_felix(felix:np.ndarray):
    """
    Muestra a felix en pantalla.
    """
    plt.imshow(felix, cmap='Greys')
    plt.show()

def felix_down(felix:np.ndarray):
    """
    Voltea a felix y luego lo muestra en pantalla.
    """
    n_filas, n_columnas = felix.shape
    nuevo_felix = np.zeros((n_filas, n_columnas), int)
    for fila in range(n_filas):
        for columna in range(n_columnas):
            nuevo_felix[fila, columna] = felix[columna, fila]
    show_felix(nuevo_felix)

felix = read_csv_and_return("TP-2_Arreglos/ejercicio_16/felix.csv")
felix_down(felix)