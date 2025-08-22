"""
Ejercicio 2

    Escribir un programa que declare un Diccionario de <entero , entero> (clave entero y significado entero) y le agrege 4 pares.
    Luego debe mostrar el diccionario por pantalla y su tamaño.

    Finalmente, redefinir 2 significados y volver a imprimir.

"""
from diccionario import Diccionario

dic = Diccionario()

dic.insert(1,2)
dic.insert(2,4)
dic.insert(3,6)
dic.insert(4,8)
print(dic)

dic[2] = 10
dic[4] = 12
print(dic)