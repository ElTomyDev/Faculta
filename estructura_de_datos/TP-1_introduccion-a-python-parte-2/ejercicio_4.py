"""
Ejercicio 4

    Escribir una función que calcule el total de una factura tras aplicarle el IVA.
    La función debe recibir el importe sin IVA y el porcentaje de IVA a aplicar,
    y devolver el total de la factura. Si se invoca la función sin pasarle
    el porcentaje de IVA, deberá aplicar un 21%.

"""

def calcular_factura_total(importe, iva=21):
    """
    Calcula y devuelve el importe mas el porcentaje del iva
    """
    return int(importe + (importe * iva / 100))

print(calcular_factura_total(1000,80))
