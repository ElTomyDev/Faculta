"""
Ejercicio 5

    En las redes sociales se produce una continua interacción y cada vez que un usuario realiza una acción, la comunidad se modifica. 
    Suponiendo que un influencer que usa Instagram cada vez que postea algo, aumenta su cantidad de seguidores según la siguiente regla:

        Durante los primeros 20 posteos, siempre suma una cantidad fija de 1000 (mil) seguidores en cada uno.
        A partir del posteo 21, la cantidad de seguidores duplica la cantidad previa de seguidores, mas 500 seguidores extra.

    Implementar una función recursiva que permita saber cuantos seguidores tendra el Instagramer luego de una cantidad determinada de posteos.
"""

def seguidoresTotal(posteos:int) -> int:
    seguidores = 0
    if posteos <= 0:
        return seguidores
    elif posteos <= 20:
        seguidores = 1000 + seguidoresTotal(posteos-1)
    else:
        seguidores = (seguidoresTotal(posteos-1) * 2) + 500
    return seguidores

print(seguidoresTotal(25))