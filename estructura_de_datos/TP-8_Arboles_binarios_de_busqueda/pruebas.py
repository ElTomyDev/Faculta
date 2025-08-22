from arbol import ABB


a = ABB()

a.insertar(5)
a.insertar(8)
a.insertar(3)
a.insertar(7)
a.insertar(9)
a.insertar(2)
a.insertar(4)

#a.insertar(2)
#a.insertar(3)
#a.insertar(6)
#a.insertar(1)
#a.insertar(4)
#a.insertar(5)
a.treePlot()
print(a.nivelDato(3))
