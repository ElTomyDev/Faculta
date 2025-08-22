"""
Ejercicio 9

    Escribir una función que dado un tiempo en horas, minutos y segundos retorne esa misma cantidad en segundos.

"""


def tiempo_a_segundos(horas, minutos, segundos):
    """
    Devuelve la cantidad de segundos que son (hora) hora, (minutos) minutos
    y (segundos) segundos.
    """
    return (((horas * 60) + minutos) * 60) + segundos

pedir_hora = int(input("Dame las horas: "))
pedir_minutos = int(input("Dame los minutos: "))
pedir_segundos = int(input("Dame los segundos: "))

print(f"{pedir_hora}:{pedir_minutos}:{pedir_segundos} son en total {tiempo_a_segundos(pedir_hora, pedir_minutos, pedir_segundos)} segundos")