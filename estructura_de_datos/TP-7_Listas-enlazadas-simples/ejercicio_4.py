"""
Ejercicio 4

    Escribir una operación del TDA Lista que elimine todas las ocurrencias de un elemento que recibe por parámetro
    y devuelva la cantidad de veces que se elimino el elemento. Se deben eliminar todos los nodos que contengan al elemento.

    Por ejemplo:

        lista1 = [ 2 , 2 , 1 , 4 , 2 , 2 , 8 , 9 , 2 , 10]

        cant = lista1.eliminarOcurrencias(2)

        Entonces, cant = 5 y lista1 = [ 1 , 4 , 8 , 9 , 10 ]
"""
from lista import Lista

class Lista(Lista):
    def eliminarOcurrencias(self,datoDel): # EliminarOcurrencias recibe como parámetro el dato que queremos eliminar
        cantDel = 0 # Inicializo mi contador de ocurrencias
        if not self.estaVacia(): # Si la lista NO está vacía
            # Hay que dividir el problema en dos partes, porque no es lo mismo eliminar el primer dato que eliminar los del medio.
            # sobretodo porque si eliminamos el primero hay que indicarle a la lista cuál es el primero:
            # Eliminamos apariciones del datoDel al inicio
            while not self.estaVacia() and self.__primero.dato == datoDel: #Mientras no esté vacía (ya validamos al principio pero si todos los números son datoDel (caso extremo) puedo terminar vaciando la lista)
                # Mientras no esté vacía y el dato que quiero eliminar es el dato contenido en el primero nodo:
                self.__primero = self.__primero.siguiente # Le indico a la lista que el primero ahora es el siguiente al que tenía definindo como primero (el primero ahora es el segundo). De esta forma ya nada me referncia al primero por lo tanto lo eliminamos
                cantDel +=1 #Sumo uno a mis datos eliminados.
            # Ahora puede ser que el que puse como primero vuelva a ser el datoDel, por eso es que estoy dentro de un while. En un caso normal donde NO está sucedineod eso, ya el while se rompre por la condición
            # Y tengo que eliminar a partir de la posición 1:
            if not self.estaVacia(): #Si no está vacía: (pudo haber quedado vacía si el único elemento que tenía para eliminar era el que eliminé en el paso anterior)
                nodoAux = self.__primero #Recorro como siempre, nodo aux será entocnes el primero referenciado por la lista
                while nodoAux.tieneSiguiente(): #Mientras nodoAux tenga siguiente:
                    if nodoAux.siguiente.dato == datoDel: #Si el dato contenido en el siguiente nodo respecto al auxiliar es el dato que quiero eliminar (si estoy en el primero estoy mirando el dato que contiene el segundo y así)
                        nodoAux.siguiente = nodoAux.siguiente.siguiente # Elimino el siguiente, diciendo que el siguiente del nodoAux es el siguiente del siguiente (me salteo uno) dejando morir al nodo que contiene el dato.
                        #Ojo acá porque como eliminé, tengo que volver a evaluar el siguiente de nodoAux, que no lo vi antes (era el siguiente del siguiente) entonces no digo que nodoAux = nodoAux.siguiente justamente porque
                        # Eliminé entonces quiero volver a correr la misma iteración porque mi "siguiente" ahora es otro que aún no vi
                        cantDel += 1 #Como eliminé, sumo uno a mi contador
                    else: #Sino, es decir, si el dato no coincide con el dato que quiero eliminar
                        nodoAux = nodoAux.siguiente # En ese caso sí me muevo en el auxiliar uno más
        return cantDel # Al final retorno cantDel que debe contener la cantidad de datos que se eliminaron

lista = Lista()
lista.agregarAlFinal(2);lista.agregarAlFinal(3);lista.agregarAlFinal(5);lista.agregarAlFinal(4);lista.agregarAlFinal(2);lista.agregarAlFinal(2)
print(lista.eliminarOcurrencias(2))
print(lista)