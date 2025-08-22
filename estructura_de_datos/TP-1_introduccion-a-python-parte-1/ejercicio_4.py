"""
Ejercicio 4:

    Implementar algoritmos que permitan:

        Calcular el perímetro y el área de un rectángulo, dada su base y su altura
        Calcular el perímetro y el área de un círculo dado su radio.

    Declarar las variables necesarias y asignarle números arbitrarios
    
"""

def perimetro_y_area_de_rectangulo(base, altura):
    """
    Devuelve el perimetro y el area de un rectangulo segun
    una (base) y (altura) dada.
    """
    perimetro = 2*base + 2*altura
    area = base * altura
    
    return base, altura, perimetro, area

def perimetro_y_area_de_circulo(radio):
    """
    Devuelve el perimetro y el area de un circulo segun
    su (radio) dado.
    """
    perimetro = 2*3.14*radio
    area = 3.14*(radio**2)
    
    return radio, perimetro, area


base, altura, rectangulo_perimetro, rectangulo_area = perimetro_y_area_de_rectangulo(20, 40)

radio, circulo_perimetro, circulo_area = perimetro_y_area_de_circulo(30)

print(f"""
      --- RECTANGULO ---
        BASE: {base} - ALTURA: {altura}
            - Perimetro: {rectangulo_perimetro}
            - Area: {rectangulo_area}
      
      --- CIRCULO ---
        RADIO: {radio}
            - Perimetro: {circulo_perimetro}
            - Area: {circulo_area}
      
      """)