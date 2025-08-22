"""
Ejercicio 3

    Escribir la operación del TDA Lista buscaElemento() que busque un elemento que recibe por parámetro. 
    La operación debe retornar una lista con las ubicaciones del elemento en la lista de entrada.

    Por ejemplo:

        lista1 = [ 2 , 2 , 1 , 4 , 2 , 8 , 9 , 2 , 10]

        posiciones = lista1.buscaElemento(2)

        Entonces, posiciones = [ 0 , 1 , 4 , 7 ]
"""
from lista import Lista

class Lista(Lista):
    def buscaElemento(self, e)->any:
        listaRetornar = Lista()
        idx = 0
        while idx < self.tamaño():
            if self.obtener(idx) == e:
                listaRetornar.agregarAlFinal(idx)
            idx += 1
        return listaRetornar

lista = Lista()
lista.agregarAlFinal(2);lista.agregarAlFinal(3);lista.agregarAlFinal(5);lista.agregarAlFinal(4);lista.agregarAlFinal(2);lista.agregarAlFinal(2)
print(lista.buscaElemento(2))