"""
Ejercicio 3

    Escribir un diccionario con sinónimos. Luego intentar insertar dos pares <clave , significado> con claves repetidas
    con la operacion insert y ver que sucede.

"""

from diccionario import Diccionario

dic = Diccionario(('listo', 'normal', 'ropa'), ('terminado', 'comun', 'vestimenta'))
print(dic)

dic['listo'] = 'finalizado'
dic.insert('normal', 'cotidiano')
print(dic)
