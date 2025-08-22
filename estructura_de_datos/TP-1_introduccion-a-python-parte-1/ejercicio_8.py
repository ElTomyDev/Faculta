"""
Ejercicio 8

    Escribir un programa que pregunte una cantidad a invertir, el interés anual y el número de años, 
    y muestre por pantalla el capital obtenido en la inversión.
    
"""

def capital_obtenido_en_la_inversion(cantidad_inversion, interes_anual, cantidad_años):
    """
    Calula la ganancia que se obtendra con la inversion en base a
    una (cantidad_inversion), (interas_anual), (cantidad_años) dada.
    """
    return (1+interes_anual/100) * cantidad_inversion * cantidad_años

pedir_cantidad_a_invertir = int(input("Dame la cantidad a invertir: "))
pedir_interes_anual = int(input("Dame el interes anual: "))
pedir_numero_años = int(input("Dame los años a invertir: "))

capital_obtenido = capital_obtenido_en_la_inversion(pedir_cantidad_a_invertir, pedir_interes_anual, pedir_numero_años)

print(f"""
      Se invirtio ${pedir_cantidad_a_invertir} pesos con un interes
      anual de ${pedir_interes_anual} pesos por unos {pedir_numero_años} años.
      
      La cantidad de capital ganado es de ${int(capital_obtenido)} pesos.
      """)
