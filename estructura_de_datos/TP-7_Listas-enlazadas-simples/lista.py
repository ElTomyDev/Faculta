import copy as cp

########################################## LISTA ##########################################

class Lista: #Definimos la clase lista

    ########################################## NODO ##########################################

    class __NodoLista: #Una lista está compuestas por nodos. Los nodos en principio no tienen sentido por fuera de nuestra clase lista, por eso lo generamos dentro
        def __init__(self, dato): #El constructor del nodo. Para crear un nodo necesitamos el dato que vamos a alojar en esa posición
            self.dato = dato # Almacenamos el dato
            self.siguiente = None # Y cada nodo contiene la información de dónde va el siguiente nodo. Por defecto, si se crea un nodo no tiene siguiente

        def tieneSiguiente(self)->bool: #Creamos el método tieneSiguiente
            return self.siguiente != None # Da True cuando hay siguiente, es decir, el siguiente no es None

    ########################################## LISTA ##########################################

    def __init__(self): # Acá ya volvimos a los métodos de listas. Inicializamos como lista vacía
        self.__primero = None #Lo único que necesita saber la lista es si tiene primero, luego el primero referencia al segundo y así.

    def estaVacia(self)->bool: #Definimos nuestra función estaVacia, que devuelve un valor booleano
        return self.__primero == None #Si el primero es None es porque está vacía (si no tiene primero no puede tener el resto)

    def __repr__(self)->str: # Definimos el repr para poder verla al hacer print
        salida = "primero" # Empezamos indicando por dónde se empeiza a contar (en nuestro caso por como estamos construyendo será de izquierda a derecha)
        nodoAux = self.__primero # Este es el clásico recorrido de listas enlazadas, tenemos un nodo auxiliar que se irá moviendo sabiendo si el nodo tiene siguiente o no. Lo inicializamos en el primero.
        #Ojo. Notar que nodoAux, si bien llama a self, self.__primero es de tipo NODO, esto va a ocurrir todo el tiempo, hay que saber si estamos trabajando a nivel LISTA o a nivel NODO
        while nodoAux != None: # Mientras el nodoAuxiliar sea DISTINTO de None:
            salida += " -> " + str(nodoAux.dato) #Salida sumará una flechita y el dato que contiene el nodo auxiliar (el que estamos viendo)
            nodoAux = nodoAux.siguiente # Una vez guardado el dato cambiamos el nodoAux al siguiente (siguiente como método de nodo). Si fuese el último el siguiente sería NONE y ahí cortaría el while
        salida += " -|" #Una vez que corta el while cerramos con un pipe
        return salida #Retornamos la salida #primero -> 2 -> 3 -> 4 -|

    def tamaño(self)->int: # Definimos tamaño que devuelve un número entero
        cantNodos = 0 #Instanciamos nuestro contador de nodos empezando en cero
        nodoAux = self.__primero # Comenzamos el clásico recorrido de listas. Creamos un nodo auxiliar y lo fijamos en el primero
        while nodoAux != None: #Mientras nodo auxiliar sea distinto de None
            cantNodos += 1 #Sumamos uno al contador
            nodoAux = nodoAux.siguiente # Nos movemos al siguiente
        return cantNodos #Retornamos el contador

    def agregarAlFinal(self, dato)->None: #Agrega un elemento al final de la lista
        nodoNuevo = Lista.__NodoLista(dato) # creo un nodo nuevo, así que instanciamos un NodoLista de la clase Lista con el dato que queremos alojar en dicho nodo
        if self.estaVacia(): #Si la lista está vacía
            self.__primero = nodoNuevo # El primer nodo será el nodo nuevo
        else: #Sino, es decir, si la lista NO está vacía (ya contiene elementos)
            nodoAux = self.__primero # definimos un nodo auxiliar como el primero
            while nodoAux.tieneSiguiente(): #Mientras el nodo auxiliar tenga siguiente. Queremos quedarnos en el último, por eso hay que ver si tiene siguiente. En este tipo de recorridos no tenemos como "volver atrás". Si llegamos hasta el None no tenemos una función del estilo "nodo anterior", por eso itera con el while hasta "tieneSiguiente"
                nodoAux = nodoAux.siguiente #El nodoAux será ahora el siguiente. Este while se corta cuando NO tenga siguiente, etnonces nodoAux será el último nodo posible (que es distinto de None)
            nodoAux.siguiente = nodoNuevo # Hacemos que el siguiente del último nodo (nodoAux) sea el nodoNuevo
    
    def insertar(self, posIns, dato)->None: #Definimos insertar que agrega un elemento a la lista pero en una posición particular, así que tomamos una posición para Insertar, un dato y no retornamos nada
        nodoNuevo = Lista.__NodoLista(dato) # Instanciamos el nodo que queremos insertar con el dato dado.
        if posIns >= 0: #Si la posición donde vamos a insertar es mayor o igual a cero (es decir, es una posición válida)
            if self.estaVacia(): # Si la lista está vacía
                self.__primero = nodoNuevo # El nuevo nodo, lo pongo primero
            elif posIns == 0: #Si NO está vacía pero la posición a insertar es 0 (la primera)
                nodoNuevo.siguiente = self.__primero #Entonces el siguiente del nodo nuevo será el que estaba originalmente como el primero (que ahora es el segundo). El resto de los nodos sigue exactamente igual (este "primero" que ahora es "segundo" sigue referenciando al "segundo" que ahora pasa a ser el "tercero" y así todo el rato)
                self.__primero = nodoNuevo # Y el primero pasa a ser el nodo nuevo.
            else: #Sino, es decir, si la lista NO está vacía y la posición a insertar es DISTINTA de 0:
                nodoAux = self.__primero # Empiezo mi recorrido sobre listas enlazadas. Defino un nodoAux que comienza en la primer posición
                posAux = 0 #Necesito ir contantdo las posiciones para saber cuándo llego a donde quiero insertar, por eso tengo que instanciar un contador inicializado en cero
                while nodoAux.tieneSiguiente() and posAux < posIns-1: #Mientas mi nodoAux tiene siguiente (En caso que me hayan dado una posición más grande que mi lista) Y (AND) la posición auxiliar es UNA ANTES de la posición donde quiero insertar (acá de nuevo, no quiero llegar hasta el final final, me quiero quedar uno antes)
                    nodoAux = nodoAux.siguiente #Nodo aux pasa a ser el siguiente
                    posAux += 1 #Sumo uno al contador
                #En este punto salí del while, así que una de dos, o NO hay siguiente o estoy en la posición anterior a donde quiero insertar el nuevo valor (nodo).
                #Acá es desición de diseño, si mi lista tiene 3 elementos y me indicaron la posición 300 se va a guardar en el final, podría lanzar una excepción, pero queda a criterio de quien desarrolle (o de quien lo pida)
                # Por ejemplo si:
                # lista = [10 , 20 , 30 , 40 , 50]
                # lista.insertar(2 , 555)
                # entonces en este punto para salir del while posAux == 1 (porque es 2 - 1)
                nodoNuevo.siguiente = nodoAux.siguiente # ENtonces el siguiente del nodoAux debe ser el 30 (que es donde quiero insertar el nuevo valor), por lo tanto el siguiente del nodoNuevo debe ser el 30
                nodoAux.siguiente = nodoNuevo # Y el nodoAux que está parado en 20 le tengo que decir que el siguiente ya no es el 30 sino que es el NodoNuevo (555)
                # lista será entonces [10 , 20 , 555 , 30 , 40 , 50]
        else: #Sino, es decir, me dieron una posición menor que cero
            raise IndexError("La posicion debe ser mayor o igual a cero") #Lanzamos una excepción. Notar que en este caso no es genérica, es un INDEX ERROR
    
    def intercambiar(self): #EJERCICIO 2
        if self.tamaño() > 1: #Si el tamaño es mayor que 2 (tengo al menos dos elementos para intercambiar)
            aux = self.__primero #Defino como auxiliar mi primer nodo
            self.__primero = aux.siguiente # Le indico a la lista que el primero es el siguiente al auxiliar (que es el primero original), es decir, el segundo. Este segundo (que ahora para la lista es el primero)
            aux.siguiente = self.__primero.siguiente # Indico que el siguiente del que originalmente estaba primero, es el siguiente del que la lista conoce como primero (tercero originalmente)
            self.__primero.siguiente = aux #Por último indico que el siguiente del que la lista considera primero es el auxiliar (el que originalmente es el primero pasa a ser el segundo)
            #FIN
            # La lógica sería así:
            # | A -> B -> C |
            # aux = A (queda flotando)
            # el siguiente de A es B, entonces pongo B primero. A estaba flotando y cree que su siguiente es B
            # self.__primero = aux.siguiente me deja un estado así = | B -> C | .... A -> B se encuentra en algún lado (en realidad se encuentra guardado en aux)
            # aux.siguiente indica que el siguiente de A debe ser self.__primero.siguiente, es decir, self.primero es B y el siguiente es C, entonces A flotante queda como A -> C porque le indiqué que el siguiente de A es el siguiente del nuevo primero
            # En este punto estoy así: |B -> C| .... A -> C, lo que quiero hacer ahora es que el siguiente de B sea A para terminar la permutación.
            # self.__primero.siguiente indica que el siguiente de B sea aux, que es A (siempre lo fue), y como A ya sabe que su siguiente es C termino generando:
            # | B -> A -> C |

    def eliminar(self, posDel)->any: #Definimos la función eliminar que recibe la posición del elemento que queremos eliminar
        datoDel = None # Inicializamos nuestra variable dato eliminado como None
        if 0 <= posDel < self.tamaño(): #Si la posición que queremos eliminar está entre 0 y el tamaño de la lista (es decir, dentro del rango válido)
            if posDel == 0: #Si la posición es 0 (es decir, queremos eliminar el primero)
                datoDel = self.__primero.dato #El dato eliminado será el dato alojado en el primer nodo
                self.__primero = self.__primero.siguiente #El primer nodo será entonces el segundo, después queda todo igual.
            else: #Sino, es decir, la posición que queremos eliminar es dinstinta de cero
                nodoAux = self.__primero #Empezamos a recorrer as always. Inicializamos nuestro nodoAuxiliar en el primero
                posAux = 0 #Empezamos a contar posiciones desde 0
                while posAux < posDel-1: # Me quiero quedar parado uno antes de la posicion a eliminar por el mismo motivo que en insertar, sino no puedo hacer nada con el nodo en el que estoy parado.
                    nodoAux = nodoAux.siguiente #Entonces mientras la posición sea menor que la anterior a la que quiero eliminar, el nodoAux será el siguiente
                    posAux += 1 #La posición se incrementa en uno
                #SALGO DEL WHILE, es decir que estoy un nodo atrás del que quiero eliminar (por construcción del while)
                datoDel = nodoAux.siguiente.dato # El dato eliminado será entonces el dato almacenado en el siguiente nodo al nodo auxiliar (el próximo)
                nodoAux.siguiente = nodoAux.siguiente.siguiente #El siguiente nodo al nodo donde estoy parado será entonces el siguiente del siguiente (me salteo uno). Y ya está!
        else: #Sino, es decir, tengo una posición para eliminar negativa o mayor al tamaño de mi lista
            raise IndexError("Posicion inválida") #Lanzamos un IndexError
        return datoDel #Retornamos el dato que eliminamos

    def obtener(self, posGet)->any: #Obtener recibe una posición y retorna el dato almacenado en esa posición
        datoGet = None # Inicializamos la variable resultado como None
        if 0 <= posGet < self.tamaño(): #Validamos el rango de posición al igual que en eliminar
            nodoAux = self.__primero #Comenzamos el recorrido como siempre. Inicializaos una variable nodoAux en el primer nodo de nuestra lista
            posAux = 0 #Inicializamos un contador de posiciones
            while posAux < posGet: #Acá no me quiero quedar uno antes (podría, pero no es necesario) porque solo quiero saber el valor del dato que tengo en esa posición, así que si llego hasta ahí no pasa nada porque no voy a modificar la lista, solo voy a consultar un elemento
                nodoAux = nodoAux.siguiente #Entonces mientras la posicion auxiliar sea menor a la que estoy buscando, me muevo al siguiente nodo
                posAux += 1 #Incremento uno a mi contador
            datoGet = nodoAux.dato #En este punto ya salí del while, es decir que posAux = posGet, por lo tanto nodoAux es el nodo que está en la posición que quiero saber el valor. Consulto en nodoAux el dato y lo guardo en datoGet. FIN
        else: #Sino, es decir, la posición es negativa o mayor al tamaño de mi lista
            raise IndexError("Posicion inválida") #Arrojamos un IndexError
        return datoGet #Retornamos el dato get

    def __getitem__(self, posGet)->any: #Cuando definimos __getitem__ estamos definiendo cómo se comporta nuestra lista si aplicamos los corchetes.
        # HACE LO MISMO QUE OBTENER, pero en vez de hacer
        # lista.obtener(3) nos permite hacer lista[3]
        # Trucazo no?
        # (Es lo mismo que veníamos haciendo con __repr__ que le indicamos cómo se debe comportar cuando le aplico print por ejemplo)
        # Esto es sobrecargar los operadores por defecto de python
        datoGet = None
        if 0 <= posGet < self.tamaño():
            nodoAux = self.__primero
            posAux = 0
            while posAux < posGet:
                nodoAux = nodoAux.siguiente
                posAux += 1
            datoGet = nodoAux.dato
        else:
            raise IndexError("Posicion inválida")
        return datoGet

    def __setitem__(self, posSet, datoSet)->None: #Así se podría sobrecargar algo del estilo "lista[3] = 555"
        #Reemplazar elemento de posicion posSet por datoSet en lista self
        pass

    def __contains__(self, datoIn)->bool: #Así se podría sobrecargar el operador IN para saber si "555 in lista" y eso retorne false o true
        #Sobrecarga del operador "in"
        pass

    def vaciar(self)->None: #Vaciar una lista es simplemente eliminar su primero (fijarlo como None)
        self.__primero = None

    def clonar(self):
        return cp.deepocopy(self) #Para clonar como es habitual tomamos la librería deepcopy

