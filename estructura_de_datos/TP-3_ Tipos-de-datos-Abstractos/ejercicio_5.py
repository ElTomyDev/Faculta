"""
Ejercicio 5

Modelar el TDA "Rectangulo" a partir de los dos lados que lo definen.

Se deben implementar las siguientes operaciones:

    Constructor: Recibe las longitudes de ambos lados
    area: calcula y devuelve el area del rectangulo
    perimetro: calcula y devuelve el perimetro
    __repr__ : imprime la longitud de los lados

Luego, modelar el TDA "Cuadrado" teniendo unicamente como variable interna en la estructura 
una variable de tipo "Rectangulo". El TDA Cuadrado debe tener las mismas operaciones que el TDA Rectangulo.

Ayuda:

    Área(Rectángulo) = lado1 * lado2

    Área(Cuadrado) = lado^2

    Perímetro(Rectangulo) = 2 * lado1 + 2 * lado2

    Perímetro(Cuadrado) = 4 * lado

"""
import numpy as np

class Rectangulo:
    def __init__(self, altura:float, ancho:float):
        self.__alto = altura
        self.__ancho = ancho
    
    def __repr__(self) -> str:
        return f"{self.__alto}x{self.__ancho}"
    
    def area(self) -> float:
        return self.__alto * self.__ancho
    
    def perimetro(self) -> float:
        return 2 *(self.__alto + self.__ancho)

class Cuadrado():
    def __init__(self, lado:float):
        self.__cuadrado = Rectangulo(lado, lado)
    
    def __repr__(self):
        return str(self.__cuadrado)
    
    def area(self) -> float:
        return self.__cuadrado.area()
    
    def perimetro(self) -> float:
        return self.__cuadrado.perimetro()
    
    
rectangulo1 = Rectangulo(20, 40)
rectangulo2 = Rectangulo(50, 50)
rectangulo3 = Rectangulo(37, 23)

print("Rectangulo:")
print(rectangulo1)
print(rectangulo1.area())
print(rectangulo1.perimetro())

cuadrado1 = Cuadrado(20)

print("Cuadrado:")
print(cuadrado1)
print(cuadrado1.area())
print(cuadrado1.perimetro())