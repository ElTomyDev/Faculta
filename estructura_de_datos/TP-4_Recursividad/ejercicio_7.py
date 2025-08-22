"""
Ejercicio 7

    Luego de una lluvia muy grande se acumula gran cantidad de agua en un estanque, durante el primer día, el agua comienza a ponerse
    de color verde y un grupo de científicos decide medir cuantas algas encuentra dentro del tanque. La primer medición le da como resultado
    12 algas. Luego deciden ir a realizar la medición todos los días para tratar de establecer un patrón de crecimiento y se encuentran que
    las algas crecen con la siguiente regla:

        Durante los siguientes 10 días (del dia 2 al 11) la cantidad de algas en el tanque es 15 más de las que había el día anterior.
        A partir del día 12, la cantidad de algas en el tanque es el triple de las que había el día previo más una cantidad fija de 100.

    Escriba una función recursiva que calcule la cantidad de algas en el tanque en un día N.

    Nota: Suponer que no mueren algas en el tanque.
    
"""

def s(arr, dato):
    idx = 0
    if idx == len(arr):
        return idx
    else:
        if arr[idx] != dato:
            idx = s(arr[0:len(arr)-2], dato) + 1
    return idx

arr1 = [2,3,4,2]
print(s(arr1, 3))

