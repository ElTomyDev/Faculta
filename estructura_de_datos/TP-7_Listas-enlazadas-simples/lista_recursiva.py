class ListaRec: # Vamos a crear el TDA Lista pero con todos los métodos que haya que iterar de forma recursiva

    
        
    ########################################## LISTA ##########################################

    #Para hacer la lista recursiva lo que vamos a hacer todo el rato es armar una función a nivel Nodo y utilizarla para hacer la vuelta recursiva, por eso antes teníamos solo dos métodos en nodo y ahora lo vamos a tener mucho más en cuenta

    def __init__(self) -> None: # El constructor es el de siempre, la lista solo sabe la ubicación del primero
        self.__primero = None

    def estaVacia(self)->bool: #Estar vacío ses lo mismo de siempre, es que el primero sea none
        return self.__primero == None

    def __repr__(self)->str: # El repr ya toma lo que construimos a nivel nodo:
        salida = "primero" # Inicia la salida con primero (como la lista que teníamos de antes)
        if not self.estaVacia(): # Si no está vacía (hay primero:)
            salida += str(self.__primero) #La salida va a ser entonces sumar el __repr__ DEL NODO
            # Entonces salida es "primero" + -> PRIMERNODO.__repr__()
            # Y el repr de PRIMERNODO llama a su siguiente (si tiene) y así hace la vuelta recursiva
        return salida + " -|" # Una vez que terminó de sumar todos los nodos cierra la salida con "-|"
    
    def agregarAlFinal(self, dato:any)->None: #Defino agregarAlFinal a nivel LISTA (toma un dato y lo agerga al final)
        nodoNuevo = ListaRec.__NodoLista(dato) # Creo un nodo nuevo
        if self.estaVacia(): # Si está vacía:
            self.__primero = nodoNuevo # El primero es nodoNuevo, no hay recursión
        else: # Sino (es decir, no está vacía)
            self.__primero.agregarAlFinalNodo(nodoNuevo) #Delego sobre el primero la responsabilidad de agregar al final el nodoNuevo
            #Pero el primero es un NODO, entonces hay que escribir a nivel nodo agragarAlFinalNodo()

    def tamaño(self)->int: #Para el tamaño
        cantNodos = 0 # Inicializo la cantidad de nodos
        if not self.estaVacia(): # Si no está vacía
            cantNodos = self.__primero.tamañoNodo() # Delego en el primer nodo la responsabilidad de contar el tamaño
        return cantNodos
    
    def insertar(self, posIns:int, dato:any)->None: #Insertar toma un dato y lo inserta en la posición recibida por parámetro
        if posIns >= 0: # Si la posición es NO NEGATIVA:
            nodoNuevo = ListaRec.__NodoLista(dato) # Creo un nodo nuevo con el dato dado
            if self.estaVacia(): # Si la lista está vacía
                self.__primero = nodoNuevo # isi, el nodoNuev es el primero
            elif posIns == 0: # Si no está vacía pero la posición que me dieron es la 0:
                nodoNuevo.siguiente = self.__primero # El siguiente del nodo nuevo será el que está primero
                self.__primero = nodoNuevo # Y ahora que tengo toda la lita atraás del nodo nuevo, inidco que el primero es el nodo nuevo
            else: # Sino, es decir, si la lista no está vacía y la posición es algún número:
                # Tengo que empezar a recorrer. Si tengo que recorrer puedo hacerlo recursivamente
                self.__primero.insertarNodo(posIns, nodoNuevo) # Delego sobre el primero la necesidad de resolver el problema
                # Ahora es un problema tipo NODO
        else: # Sino (si la posIns es negativa)
            raise IndexError("Posición inválida") # Lanzo un IndexError
    
    def eliminar(self, posDel:int)->any: # Definimos eliminar como método de lista
        datoDel = None # Como es habitual, voy a retornar el dato que elimino
        if 0 <= posDel < self.tamaño(): # Si la posición está entre 0 y el tamaño de la lista (menos 1 porque es <) - Es decir, estoy preguntando si la posición existe dentrod el arreglo
            if posDel == 0: # Si la posición es la primera
                datoDel = self.__primero.dato # Entonces el dato a eliminar es el dato almacenado en el primer nodo
                self.__primero = self.__primero.siguiente # El primero es, entonces, el siguiente
            else: #Sino, es decir, si la posición no es la primera:
                datoDel = self.__primero.eliminarNodo(posDel) # Recorro recursivamente con eliminarNodo (empezando del primero)
        else: #Sino, es decir, me dieron un índice negativo o uno más alto que el tamaño de mi lista
            raise IndexError("Posición inválida") # Lanzo un Index Error
        return datoDel #Retorno el dato del nodo que eliminé
    
    def obtener(self, posGet:int)->any: #Obtener es muy parecido a eliminar (pero más fácil porque no tengo que cambiar conexiones entre los nodos)
        datoGet = None # Inicializo la variable que contendrá el valor de la posición indicada
        if 0 <= posGet < self.tamaño(): # Si el índice es válido (es positivo y menor estricto que el tamaño)
            datoGet = self.__primero.obtenerNodo(posGet) # Delego en el primero la responsabilidad de saber qué nodo es
        else: # Sino, es decir, me dieron una posición inválida
            raise IndexError("Posicion inválida") # Lanzo un index error
        return datoGet # Retorno el dato
    
    def intercambiar(self) -> None:
        if not self.estaVacia():
            self.__primero.intercambiarNodo()
    
    ########################################## NODO #########################################
    class __NodoLista: # Igual que antes, una lsita esta compuesta de nodos
        def __init__(self, dato) -> None: # El constructor del nodo es el mismo, toma un dato
            self.dato = dato # Guarda el dato internamente
            self.siguiente = None # Y tiene la información de su siguiente

        def tieneSiguienteNodo(self)->bool: # Creamos una función tiene siguiente
            return self.siguiente != None # Simplemente evalúa si el siguiente es None o no. Si es None, no tiene siguiente

        def __repr__(self)->str: #Acá ya empieza a cambiar respecto a la interfaz anterior.
            # Hay que notar que el __repr__ está definido a nivel NODO, antes no lo estaba.
            # El chiste con las listas recursivas es delegar mucha funcionalidad en los nodos
            salida = "" # Inicializamos una variable string vacía para la salida
            if self != None: # Si el Nodo es distinto de None:
                salida = f" -> {self.dato}" #La salida es entonces el valor del dato (y las flechitas para darle formato)
                if self.tieneSiguienteNodo(): # Y si tiene siguiente:
                    salida += str(self.siguiente) # La salida agrega el __repr__ del siguiente
                    # Recordar que hacer str(unObjeto) es lo mismo que pedir unObjeto.__repr__()
            return salida # Retornamos la salida

        def agregarAlFinalNodo(self, nodoNuevo)->None:#AgregarAlFinalNodo toma UN NODO, no un dato como en la lista
            if not self.tieneSiguienteNodo(): # Si el nodo en el que estoy parado no tiene siguiente
                self.siguiente = nodoNuevo # El siguiente es el nodoNuevo
            else: #Sino
                self.siguiente.agregarAlFinalNodo(nodoNuevo) # Me muevo al siguiente y agrego el nodoNuevo
        
        def tamañoNodo(self)->int: #Tamaño nodo
            cantNodos = 0 # Que inicializa la variable que después le va a pasar a la función de lsita
            if self != None: # Si el nodo en el que estoy aprado es distinto de none:
                cantNodos = 1 # Cantidad de nodos es 1
                if self.tieneSiguienteNodo(): # Si además, tiene siguiente
                    cantNodos += self.siguiente.tamañoNodo() # Voy a sumar el nodo siguiente, así hago la vuelta recursiva
            return cantNodos # Finalmente retorno la cantidad de nodos
        
        def insertarNodo(self, posIns, nodoNuevo, posActual = 0): # De alguna forma tengo que acumular las posiciones para contar cuánto me voy moviendo. Como hicimos con tamaño pero ahora recibiendo como parámetro
            if posActual == posIns-1 or not self.tieneSiguiente():
                # Si la posActual es LA ANTERIOR a donde quiero insertar O no hay siguiente -> Esto también quiere decir que si me dieron un valor que está fuera de índice no importa y lo coloca al último
                # Notar acá que pasa lo mismo que en las no-recursivas. Tengo que estar atentx a si necesito llegar hasta ese nodo o me tengo que quedar
                # Acá solo entro en esa posición si se cumple la condición, no es como el while que entraba siempre
                nodoNuevo.siguiente = self.siguiente # Entonces el siguiente del nodoNuevo es el siguiente del que estoy parado (el que está en el lugar donde quiero insertar)
                self.siguiente = nodoNuevo # Por lo tanto mi siguiente es el nodo nuevo
            else: #Sino, es decir, si la posActual NO ES la anterior a donde quiero insertar y tengo siguiente
                self.siguiente.insertarNodo(posIns, nodoNuevo, posActual+1) # La responsabilidad es del siguiente nodo, aumento 1 en posActual
        
        def eliminarNodo(self, posDel, posActual = 0)->any:
            #recorro lista recursivamente hasta que self apunte al nodo posDel-1 y borro
            datoDel = None # Necesito obtener el datoDel porque es lo que retorna eliminar
            if posActual == posDel-1: # Si la posición es la anterior a la que quiero elimianr
                datoDel = self.siguiente.dato # me guardo el dato del nodo que quiero eliminar, el siguiente del que estoy parado (self)
                self.siguiente = self.siguiente.siguiente # Entonces mi siguiente no es el que borro sino su siguiente
            else: # Sino, es decir, si la posición no es la que me interesa
                datoDel = self.siguiente.eliminarNodo(posDel, posActual+1) # El siguiente nodo será el encargado de eliminar y evaluar. Incremento una posición
            return datoDel # Retorno el dato a eliminar
        
        def obtenerNodo(self, posGet, posActual = 0)->any: # La función cuenta la posActual
            datoGet = None # Inicializo la variable con el dato que quiero obtener
            if posActual == posGet: # Si la posicióna actual es la que estoy buscando:
                datoGet = self.dato # Guardo eld ato
            else: # Sino
                datoGet = self.siguiente.obtenerNodo(posGet, posActual+1) # Me muevo recursivamente al siguiente nodo
            return datoGet #Retorno finalmente el datoGet
        
        def intercambiarNodo(self):
            
        