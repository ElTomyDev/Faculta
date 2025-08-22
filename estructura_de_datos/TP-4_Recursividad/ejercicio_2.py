"""
Ejercicio 2

    Una canilla de una casa pierde agua de forma que todos los días pierde 2 gotas más que el día anterior. 
    Escribir una función recursiva que calcule cuantas gotas perderá la canilla el día N. El primer día solo perdía dos gotas.

    De manera opcional, con un ciclo que llame N veces a la función recursiva,calcular la cantidad de gotas acumuladas en N días.
    dia     cantgotas   cant acum
     1          2           2
     2          4           6
     3          6           12
     4          8           20
    
"""

def calcular_gotas_perdidas(N:int) -> int:
    gotas = 0
    if N != 0:
        gotas = 2 + calcular_gotas_perdidas(N-1)
        #print(f"dia: {N} - gotas: {gotas}")
        return gotas
    return gotas

def cantAcumuladas(N:int) -> int:
    acum = 0
    if N != 0:
        acum = cantAcumuladas(N-1) + calcular_gotas_perdidas(N)
        print(f"| Dia = {N} | CantGotas = {calcular_gotas_perdidas(N)} | CantAcum = {acum} |")
        return acum
    return acum

cantAcumuladas(4)
