"""
Ejercicio 5

    Escribir la función máximo, que recibe 2 números por parámetro
    y retorna el mayor. Luego, usando esta función, escriba un programa
    que pida 10 números al usuario por teclado y al finalizar informe el mayor por pantalla.

"""

def maximo_entre_valores(valor1, valor2):
    """
    Devuelve el mayor entre (valor1) y (valor2)
    """
    return max(valor1, valor2)

def mayor_e_entre_dies():
    """
    Pide 10 numeros al usuario y se queda con el mas grande.
    """
    
    mas_grande = 0
    contador = 1
    while contador <= 10:
        numero = int(input("Dame un numero: ")) 
        mas_grande = maximo_entre_valores(mas_grande, numero)
        contador += 1
    
    return(mas_grande)

print(mayor_e_entre_dies())