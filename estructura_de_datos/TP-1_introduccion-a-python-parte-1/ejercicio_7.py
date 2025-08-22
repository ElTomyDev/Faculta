"""
Ejercicio 7

    Escribir un programa que pida un peso (en kg) y una estatura (en metros), 
    calcule el índice de masa corporal y lo almacene en una variable. Luego debe 
    mostrar por pantalla la frase: "El índice de masa corporal es: <imc>". 
    Donde <imc> es el índice de masa corporal calculado.


"""

def calcular_imc(peso, altura):
    """
    Calcula y devuelve el indice de masa corporal segun un (peso)
    y una (altura) dada.
    """
    return peso / (altura*altura) 

pedir_peso = int(input("Dame tu peso en kg: "))
pedir_altura = float(input("Dame tu altura en metros: "))

imc_calculado = calcular_imc(pedir_peso, pedir_altura)

print(f"El indice de masa corporal es : < {imc_calculado:.1f} >")

