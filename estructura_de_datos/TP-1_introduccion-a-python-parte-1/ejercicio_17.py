"""
Ejercicio 17

    Para pagar un determinado impuesto se debe ser mayor de 18 años 
    y tener unos ingresos iguales o superiores a $100000 mensuales. 
    Escribir un programa que pregunte la edad y los ingresos mensuales 
    y muestre por pantalla si se debe pagar o no.
    
"""

def verificar_si_debe_pagar_impuestos(edad, ingresos):
    """
    Devuelve una cadana que indica si debe o no pagar impuestos
    segun una (edad) y unos (ingresos) mensuales dados.
    """
    return "debe pagar impuestos" if edad >= 18 and ingresos >= 100000 else "no debe pagar impuestos"

pedir_edad = int(input("Dame tu edad: "))
pedir_ingresos = int(input("Dame tus ingresos mensuales: "))

print(f"""
      < EDAD: {pedir_edad} - INGRESOS MENSUALES: {pedir_ingresos} >
      
      - Usted {verificar_si_debe_pagar_impuestos(pedir_edad, pedir_ingresos)}.
    """)