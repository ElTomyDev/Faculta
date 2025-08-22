from graphviz import Digraph
import copy as cp
import numpy as np

class ABB: # Creamos la clase árbol de busqueda binario
    def __init__(self): # Un árbol es solo una referencia a su raíz (que será un NODO)
        self.__raiz = None # Lo instanciamos con la raiz inicializada en None

    def estaVacio(self)->bool: # Estar vacío (no contener información) es igual a que la raíz sea NONE
        return self.__raiz == None

    def vaciar(self)->None: # Vaciar es asignar como None a la raiz
        self.__raiz = None

    def clonar(self): #Para clonar como hicimos con otras estructuras de datos, usamos deepcopy
        return cp.deepcopy(self)

    def treePlot(self, fileName='TP-8_Arboles_binarios_de_busqueda/arbol')->None: # Cremos un método para plotear el árbol
        if not self.estaVacio(): # Si no está vacío:
            treeDot = Digraph() # Instanciamos un objeto Digraph() vacío
            treeDot.node(str(self.__raiz.dato), str(self.__raiz.dato)) # Le pasamos el nodo raiz (el nombre del nodo coincide con el dato almacenado)
            # https://networkx.org/documentation/stable/reference/classes/digraph.html siempre es bueno revisar la documentación si no entendemos algo
            self.__raiz.treePlot(treeDot) # Ahora para completar los nodos que nos faltan usamos treePlt pero SOBRE RAÍZ, es decir que es un método de NODO, no de árbol
            treeDot.render(fileName, view=True) # Finalmente renderizamos la imagen del árbol

    def insertar(self, dato:int)->None: # Insertar toma un dato y no retorna nada
        nodoNuevo = ABB.__NodoArbol(dato) # Creamos un nuevo nodo
        if self.estaVacio(): # Si mi arbol está vacío
            self.__raiz = nodoNuevo # El nuevo nodo será la raíz
        else: # Sino, es decir, ya tengo datos en el árbol
            self.__raiz.insertarNodo(nodoNuevo) # Delegamos en la raíz la responsabilidad de ubicar el nuevo nodo
    
    def mostrarPreOrden(self)->None: #Preorden es ir procesando los nodos a medida que los recorro
        if not self.estaVacio(): # Si no está vacío
            self.__raiz.mostrarPreOrdenNodo() # Delego en la raíz la responsabilidad de mostrar el preOrden
    
    def mostrarPostOrden(self)->None: # El posorden es procesar el dato una vez recorrido el árbol
        if not self.estaVacio(): # Si no está vacío
            self.__raiz.mostrarPostOrdenNodo() # Empiezo por la raíz
    
    def mostrarInOrden(self)->None: #Ahora mostrar in order es hacerlo en la mitad enter un arbol y el otro
        if not self.estaVacio(): # COmo siempre, si no está vacío
            self.__raiz.mostrarInOrdenNodo() # Delego en la raíz la responsabilidad

    def peso(self)->int: # El peso del árbol es la cantidad de nodos que tiene
        cantNodos = 0 # Inicializamos una variable en 0 para contar
        if not self.estaVacio(): # Si no está vacío
            cantNodos = self.__raiz.pesoNodo() # Le digo a raiz que cuente la cantidad de nodos
        return cantNodos # finalmente retorno la cantiad de nodos
    
    def buscar(self, datoBusc)->bool: # Buscar en un árbol toma un dato por parámetro y devuelve un booleano indicando s el dato está en el árbol o no
        encontrado = False # Inicilizamos una variable como False, podría ser None también
        if not self.estaVacio(): # Si no está vacío:
            encontrado = self.__raiz.buscarNodo(datoBusc) != None # Quiero ver si encontré un nodo distinto de None que contenga el dato (si no lo cotiene será None)
        return encontrado # Retorno la variable encontrado

    def profundidad(self)->int: # La profundidad es cuántos niveles de hijos hay
        profTotal = 0 #empieza en cero
        if not self.estaVacio(): # Si no está vacío:
            profTotal = self.__raiz.alturaNodo() # Le pregunto a la raiz la altura del nodo
        return profTotal # Devuelvo la profundidad total

    def nivelDato(self, datoBusc)->int: # QUeremos saber en qué nivel está un dato recibido por parámetro
        nivelDatoBusc = None # Inicialmente el nivel es None. Si el dato no está en el arbol queremos retornar none
        if not self.estaVacio(): # Si el arbol NO está vacío
            nivelDatoBusc = self.__raiz.nivelDatoNodo(datoBusc) # Buscamos a partir de la raíz en qué nivel está el dato buscado
        return nivelDatoBusc # Retornamos el nivel del dato buscado
    
    def maximo(self)->int: #Retorna el valor del maximo o None si self esta vacio
        datoMaximo = None
        if not self.estaVacio():
            datoMaximo = self.__raiz.maximoNodo().dato
        return datoMaximo
    
    def minimo(self)->int: #Retorna el valor del minimo o None si self esta vacio
        datoMinimo = None
        if not self.estaVacio():
            datoMinimo = self.__raiz.minimoNodo().dato
        return datoMinimo
    
    def eliminar(self, datoDel:int)->None: #La función eliminar toma un dato a eliminar
        if not self.estaVacio(): # Si no está vacío:
            if self.__raiz.dato == datoDel: # Y si la raiz contiene el dato que qeuremos eliminar:
                # Acá hay que decidir si pongo como nueva raíz al izquierdo o al derecho, decisión de diseño por cuál empezamos a probar:
                nodoReemplazo = self.__raiz.predecesor() # Elegimos el predecesor, es decir, el número más grande que sea más chico que (en este caso) la raíz
                if nodoReemplazo==None:  # Si el predecesor (nodoReemplazo) es None (no hay predecesor)
                    nodoReemplazo = self.__raiz.sucesor() # Entonces el nodoReemplazo debe ser el sucesor
                if nodoReemplazo != None: # Si el nodoReemplazo es DISTINTO de None, es decir, encontré un sucesor (o predecesor)
                    self.__raiz.eliminarNodo(nodoReemplazo.dato) # Elimino el nodo que contiene el dato del sucesor (o predecesor) (porque sino lo tendría dos veces) (como es un método de nodo invoco a la raíz solo para poder usar el método)
                    nodoReemplazo.izquierdo = self.__raiz.izquierdo # Al nodoReemplazo le asigno como izquiero lo que tenga la raíz es su izquierdo
                    nodoReemplazo.derecho = self.__raiz.derecho # Y como derecho el subarbol derecho respecto de la raiz
                    self.__raiz = nodoReemplazo # Le indico al árbol que su nueva raíz es, entonces, el nodoReemplazo
            else: #Sino, es decir, el dato que quiero eliminar no es el que está contenido en el nodo raíz
                self.__raiz.eliminarNodo(datoDel) # Delego en la raíz la responsabilidad de eliminar el nodo
    
    def cantHojas(self) -> int: # Ejercicio 2
        cantidadHojas = 0 # Inicio la cantidad de hojas en 0
        if not self.estaVacio(): # Si el nodo raiz no es igual a None
            cantidadHojas = self.__raiz.cantHojasNodo() # Delego la responsabilidad al nodo de contar las hojas
        return cantidadHojas
    
    def mostrarNivel(self, nivel:int) -> np.ndarray: # Ejercicio 3
        if not self.estaVacio(): # Si no esta vacio
            self.__raiz.mostrarNivelNodo(nivel) # deriba la responsabilidad al nodo de guardar los nodos del nivel indicado
        
        
    
    ##################################################################
    ##################################################################
    class __NodoArbol: # Ahora creamos la clase nodo, dentro del TDA árbol
        def __init__(self, dato): # Para instanciarlo necesitamos un dato
            self.dato = dato # Guardamos el dato
            self.izquierdo = None # Y el árbol va a tener una referencia izquierda
            self.derecho = None # Y una referncia derecha.

        def tieneIzquierdo(self)->bool: # Creamos métodos auxiliares para saber si un nodo tiene izquiedo
            return self.izquierdo != None # Es decir, su izquierdo es distinto de None

        def tieneDerecho(self)->bool: # Análogamente queremos saber si un nodo tiene derecho
            return self.derecho != None # Es decir, su derecho es distinto de None

        def grado(self)->int: # El grado de un nodo es la cantidad de hijos que tiene
            cantHijos = 0 # Inicilamente es cero
            if self.tieneIzquierdo(): cantHijos += 1 # Si tiene izquierdo suma 1
            if self.tieneDerecho(): cantHijos += 1 # Si tiene derecho también suma 1
            return cantHijos # Retorna la cantidad de hios (grado)

        def esHoja(self)->bool: # Es Hoja si no tiene hijos (ni izquierdo ni derecho)
            return self.grado() == 0 # Es lo mismo que pedir grador 0

        def treePlot(self, dot:Digraph)->None: # Esta función treePlot es A NIVEL NODO, esa diferecnia tiene con treePlot a nivel ÁRBOL
            if self.tieneIzquierdo(): # Si tiene izquierdo:
                dot.node(str(self.izquierdo.dato), str(self.izquierdo.dato)) # Agrego un nodo al gráfico (el que corresponde al izquierdo)
                dot.edge(str(self.dato), str(self.izquierdo.dato)) # Armo una conexión entre el nodo (self) y su izquierdo (self.izquierdo)
                self.izquierdo.treePlot(dot) # Hago un llamado recursivo sobre izquierdo, esto validará si izquierdo tiene hijos y así hará la vuelta recursiva
            else: #sino, es decir, no tiene izquierdo
                dot.node("-"+str(self.dato)+"l", "-") # Creo un nodo ficticio para ilustrar en el gráfico que no hay izquierdo (por eso la L (left))
                dot.edge(str(self.dato), "-"+str(self.dato)+"l") # Creo la conexión enter self y ese nodo ficticio
            if self.tieneDerecho(): # Para el lado derecho es totalmente análogo cada paso
                dot.node(str(self.derecho.dato), str(self.derecho.dato))
                dot.edge(str(self.dato), str(self.derecho.dato))
                self.derecho.treePlot(dot)
            else:
                dot.node("-"+str(self.dato)+"r", "-")
                dot.edge(str(self.dato), "-"+str(self.dato)+"r")
    
        def insertarNodo(self, nodoNuevo)->None: # InsertarNodo traerá el dato que se le pasó a insertar como parámetro y no retorna nada
            if nodoNuevo.dato < self.dato: # Si el dato contenido en el nodoNuevo es menor que el dato almacenado en el nodo en el que estoy parado (raíz si fuese la primer iteración):
                #El nuevo nodo va a la izquierda de self
                if not self.tieneIzquierdo(): # Y si NO tengo izquierdo:
                    self.izquierdo = nodoNuevo # El izquierdo de SELF será entonces la raíz
                else: #Sino, es decir, TENGO IZQUIERDO
                    self.izquierdo.insertarNodo(nodoNuevo) # Delego en el izquierdo la responasbilidad de acomodar el nuevo nodo
            elif nodoNuevo.dato > self.dato: # Sino, si el dato almacenado en el nodoNuevo es MAYOR que el dato de self (nodo en el que estoy parado, raíz si es la primera iteración):
                #El nuevo nodo va a la derecha de self
                if not self.tieneDerecho(): # Si NO tengo derecho
                    self.derecho = nodoNuevo # Entonces el derecho de self será nodoNuevo
                else: # Sino, es decir, TENGO DERECHO
                    self.derecho.insertarNodo(nodoNuevo) # Delego en el derecho la responsabiliad de insertar el nuevoNodo
            else: # Sino, es decir, el dato no es menor ni es mayor al de self (esto significa que el dato COINCIDE con el dato de self)
                raise Exception("No se admiten datos repetidos") # lanzo una excepción: en un árbol de búsqueda binario NO PUEDE haber número repetidos
        
        def mostrarPreOrdenNodo(self)->None: # mostrar preorden que comienza en la raíz
            print(self.dato) # Primero printeo el dato almacenado en el nodo que me muevo
            if self.tieneIzquierdo(): # Luego, si tiene izquierdo, avanzo sobre el árbol izquierdo
                self.izquierdo.mostrarPreOrdenNodo() # delegando en el izquierdo la responsabilidad de mostrar el pre-orden
            if self.tieneDerecho(): # Y análogamente lo mismo para el derecho
                self.derecho.mostrarPreOrdenNodo() # Recorro el subarbol derecho
        
        def mostrarPostOrdenNodo(self)->None:
            if self.tieneIzquierdo(): # Si tiene izquierdo:
                self.izquierdo.mostrarPostOrdenNodo() # Recorro primero el subarbol izquierdo
            if self.tieneDerecho(): # Si tiene derecho
                self.derecho.mostrarPostOrdenNodo() # Recorro el subarbol derecho
            print(self.dato) # Una vez llegado al último, proceso el dato
        
        def mostrarInOrdenNodo(self)->None: # Escribo mi método a nivel nodo
            if self.tieneIzquierdo(): # Empiezo recorriendo el izquierdo. Esto es clave porque va a determinar cómo se organizan mis números
                self.izquierdo.mostrarInOrdenNodo() # Al comenzar por el izquierdo, como mi árbol acomoda los datos menores a la izquierda
            print(self.dato) # Me va a mostrar los datos del menor al mayor
            if self.tieneDerecho(): # Si empiezo por el derecho me va a mostrar mis datos de mayor a menor
                self.derecho.mostrarInOrdenNodo()
        
        def pesoNodo(self)->int: # defino el método pesoNodo
            cantNodos = 1 # Inicializo en 1 porque ya estoy en un nodo (raíz) entonces por lo menos uno ya tengo
            if self.tieneIzquierdo(): # Si tiene izquierdo:
                cantNodos += self.izquierdo.pesoNodo() # sumo en cantNodos el peso del subárbol izquierdo
            if self.tieneDerecho(): # Y si tiene derecho:
                cantNodos += self.derecho.pesoNodo() # sumo en cantNodos el peso del subarbol derecho
            return cantNodos # Retorno cantNodos
        
        def buscarNodo(self, datoBusc): # Ahora lo armo a nivel nodo
            #Si el datoBusc esta en el arbol retorna el nodo que lo contiene, porque la función a nivel ARBOL compara contra None, entonces nosotros no queremos devolver un booleano en esta función, sino un NODO
            #Si el datoBusc NO estan en el arbol retorna None
            nodoDatoBusc = None #Inicializamos la varibale del nodoBuscado como none
            if self.dato == datoBusc: # Si el dato contenido en el nodo sobre el que estoy parado es igual al dato buscado:
                nodoDatoBusc = self # El nodo buscado es SELF
            else: # Sino, es decir, el dato contenido en el nodo que estoy parado NO coincide con el dato buscado:
                if datoBusc < self.dato: # Si el dato buscado es MENOR que el dato almacenado en el nodo actual:
                    if self.tieneIzquierdo(): # Y si el nodo actual TIENE IZQUIERDO:
                        nodoDatoBusc = self.izquierdo.buscarNodo(datoBusc) # El nodo que contiene el dato que estoy buscando deberá estar en el lado izquierdo
                else: #sino, es decir, el dato buscado es MAYOR que el dato almacenado en el nodo actual
                    if self.tieneDerecho(): # y además, el nodo actual TIENE DERECHO
                        nodoDatoBusc = self.derecho.buscarNodo(datoBusc) # El nodo que contiene el dato que estoy buscando deberá estar en el lado derecho:
            return nodoDatoBusc # Retorno, finalmene, el nodo que contiene el dato buscado en caso que exista, None en caso contrario
                
        def alturaNodo(self)->int: # Mi función retornará un entero que me dice la profundidad de ese nodo
            alturaIzq = 0 # Como cada nodo se me puede dividir en dos, voy a tener por un lado, la altura del arbol izquierdo, la del derecho, y la del nodo mismo (self)
            alturaDer = 0 # Todas las variables inicializadas en 0
            alturaSelf = 0 # Por ejemplo un arbol que sea solo raíz tendrá profundidad cero
            if not self.esHoja(): # Si NO es hoja, es decir, tiene algún hijo
                if self.tieneIzquierdo(): # Si tiene izquierdo
                    alturaIzq = self.izquierdo.alturaNodo() # sigo contando la altura del subarbol izquierdo
                if self.tieneDerecho(): # Si tiene derecho:
                    alturaDer = self.derecho.alturaNodo() # Sigo contando la altura del subarbol derecho
                    alturaSelf = 1 + max(alturaIzq, alturaDer) # La altura propia del nodo es entonces, 1 (del propio nodo) + la más grande entre las alturas izquiedas o derechas
            return alturaSelf # Retorno la altura self, que es la que me interesa
        
        def nivelDatoNodo(self, datoBusc, nivelActual = 0)->int: # Tomamos el dato buscado y una variable nivelActual inicializada en cero
            nivelDatoBusc = None # Con el mismo critero de antes inicilizamos en None
            if self.dato == datoBusc: # Si el dato almacenado en el nodo es el dato buscado
                nivelDatoBusc = nivelActual # El nivel del dato buscado es el actual, así que ya terminamos
            elif self.dato > datoBusc: #Sino, si el dato que está almacenado en el nodo es MAYOR que el dato buscado:
                if self.tieneIzquierdo(): # Si tiene izquierdo, busco en el subarbol izquierdo
                    nivelDatoBusc = self.izquierdo.nivelDatoNodo(datoBusc, nivelActual+1) # Pero tengo que sumar 1 al nivel actual
            else: # sino, es decir, el dato almacenado en el nodo MENOR que el dato que estoy busancod:
                if self.tieneDerecho(): # Si tengo derecho
                    nivelDatoBusc = self.derecho.nivelDatoNodo(datoBusc, nivelActual+1) #Buco en el derecho (incrementando uno al nivel)
            return nivelDatoBusc # Retorno el nivel del dato buscado
        
        def maximoNodo(self):#->ABB.__NodoArbol: #que contiene el valor maximo del
                                                 #subarbol del cual self es la raiz
            nodoMaximo = self # Hasta que enuentre uno más grande, el máximo es si mismo (self)
            if self.tieneDerecho(): # Si hay derecho, es decir, hay nodos con datos mayores al dato almacenado en self
                nodoMaximo = self.derecho.maximoNodo() # el nodo máximo habrá que buscarlo en el derecho
            return nodoMaximo # Retorno el nodo máximo

        def minimoNodo(self):#->ABB.__NodoArbol:# que contiene el valor minimo del
                                                #subarbol del cual self es la raiz
            nodoMinimo = self
            if self.tieneIzquierdo(): # Acá la misma lógica que antes, si hay izquierdo es porque hay un nodo que contiene un dato menor al que estoy mirando
                nodoMinimo = self.izquierdo.minimoNodo() # Recorro los árboles izquierdos
            return nodoMinimo

        def predecesor(self):#->ABB.__NodoArbol que contiene el valor maximo del subarbol izquierdo
            nodoPredecesor = None # Esto es definición, quiero el nodo que contenga el dato más grande de mi subarbol izquierdo
            if self.tieneIzquierdo(): # entonces si tengo izquierdo
                nodoPredecesor = self.izquierdo.maximoNodo() # será el más grande
            return nodoPredecesor

        def sucesor(self):#->ABB.__NodoArbol que contiene el valor minimo del subarbol derecho
            nodoSucesor = None # la misma lógica pero al revés, quiero el nodo que contenga el dato más chico dentro de mi subarbol derecho
            if self.tieneDerecho(): # Entonces si tiene derecho
                nodoSucesor = self.derecho.minimoNodo() # le pido el mínimo
            return nodoSucesor
        
        def buscarProgenitor(self, datoBusc:int):#->tuple[ABB.__NodoArbol, ABB.__NodoArbol, str]
                                                #[progenitor, hije, "izq"/"der"]
            # Para eliminar nodo necesito la función auxiliar buscarProgenitor.
            # Buscar progenitor es una función de NODO que toma el dato buscado y devuelve una tupla de tres elementos
            # El primer elemento es el nodoProgenitor
            # El segundo elemento es el nodoHije
            # El tercer elemento indica si el nodoHije está a la izquierda o a la derecha del progenitor
            nodoProgenitor = nodoHije = lado = None # Notación de Python, inicializo tres variables todas como None
            if datoBusc < self.dato: # Si el datoBuscado es MENOR al dato contenido en el nodo donde estoy parado:
                if self.tieneIzquierdo(): # Y si el nodo donde estoy parado tiene izquierdo:
                    if self.izquierdo.dato == datoBusc: # Y si el dato almacenado en el nodo izquierdo coincie con el dato buscado, entonces
                        nodoProgenitor = self # El progenitor es el nodo en el que estoy parado
                        nodoHije = self.izquierdo # El nodo hije es el izquierdo
                        lado = "izq" # Me guardo la información de que el hije es el izquierdo
                else: #Sino, es decir, el dato almacenado en el nodo izquierdo NO COINCIDE con el dato buscado (pero sí sucede que el dato buscado es menor al dato en self y además self tiene izquierdo:)
                    nodoProgenitor, nodoHije, lado = self.izquierdo.buscarProgenitor(datoBusc) # Sigo buscando en el izquierdo el nodo que contenga el dato, su progenitor y si es el izquierdo o el derecho
            elif datoBusc > self.dato: # Sino, si el dao to buscado es MAYOR al dato almacenado en el nodo donde estoy parado
                if self.tieneDerecho(): # Y si el nodo en el que estoy parado tiene derecho
                    if self.derecho.dato == datoBusc: # Y si el nodo derecho contiene el dato que estoy buscando
                        nodoProgenitor = self # El progenitor es el nodo anterior al nodo que contiene el dato
                        nodoHije = self.derecho # EL nodo hije es el nodo que contiene el dato
                        lado = "der" # Y en este caso, es el que está a la derecha del progenitor
                else: #Sino, es decir, el dato almacenado en el nodo derecho NO COINCIDE con el dato buscado, pero sí sucede que el dto buscado es mayor al dato en self y además, self tiene derecho
                    nodoProgenitor, nodoHije, lado = self.derecho.buscarProgenitor(datoBusc) # Sigo buscando del lado derecho
            return nodoProgenitor, nodoHije, lado # Al final del día retorno la tupla con los tres elementos

        def eliminarNodo(self, datoDel:int)->None: #Con buscarProgenitor armada, puedo escribir facilmente elimianrNodo
            nodoReemplazo = None # Con la misma lógica que hicimos con la raíz, tenemos el nodo que va a reemplazar al que estamos eliminando
            nodoProgenitor, nodoAEliminar, lado = self.buscarProgenitor(datoDel) # Guardo nodoProgenitor, nodoAEliminar y el lado usando la función auxiliar
            if nodoProgenitor != None: # Si el nodo progenitor es distinto de None (es decir, existe el elemento que quiero eliminar, dado que todo elemento que no sea raíz tiene un progenitor)
                nodoReemplazo = nodoAEliminar.predecesor() # Igual que con la raíz, el nodoReemplazo es el predecesor (podría empezar por cuestion de diseño con el sucesor)
                if nodoReemplazo == None: # Si el nodoReemplazo es None, es decir, no existía el predecesor:
                    nodoReemplazo = nodoAEliminar.sucesor() # Entoncse el nodoReemplazo será el sucesor
                if nodoReemplazo != None: # Si el nodoReemplazo es distinto de None (o es el sucesor o es el predecesor)
                    self.eliminarNodo(nodoReemplazo.dato) # Elimino el nodo que voy a usar para reemplazar (como es sucesor o predecesor es hoja por definición)
                    nodoReemplazo.izquierdo = nodoAEliminar.izquierdo # Le asigno al nodoReemplazo como izquierdo el subarbol izquierdo que tenía el nodo a eliminar
                    nodoReemplazo.derecho = nodoAEliminar.derecho # Análogamente con el lado derecho
                if lado == "izq": # Si era hije izquierdo
                    nodoProgenitor.izquierdo = nodoReemplazo # Le indico al progenitor que su nuevo hije izquierdo es el nodoReemplazo
                elif lado == "der": # Si era hije derecho
                    nodoProgenitor.derecho = nodoReemplazo # Le inidco al progenitor que su nuevo hije derecho es el nodoReemplazo

        def cantHojasNodo(self) -> int: #Ejercicio 2 
            cantidad = 0
            if self.esHoja():
                cantidad += 1
            elif self.tieneDerecho() and self.tieneIzquierdo():
                cantidad = self.izquierdo.cantHojasNodo() + self.derecho.cantHojasNodo()
            elif self.tieneIzquierdo():
                cantidad = self.izquierdo.cantHojasNodo()
            else:
                cantidad = self.derecho.cantHojasNodo()
            return cantidad
        
        def mostrarNivelNodo(self, nivel: int, nivelActual:int=0) -> None: # Ejercicio 3
            if nivelActual == nivel:
                print(self.dato)
            else:
                if self.tieneDerecho():
                    self.derecho.mostrarNivelNodo(nivel, nivelActual+1)
                if self.tieneIzquierdo():
                    self.izquierdo.mostrarNivelNodo(nivel, nivelActual+1)
                    

        
        
        
        
        