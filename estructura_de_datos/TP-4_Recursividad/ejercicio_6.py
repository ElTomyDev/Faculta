"""
Ejercicio 6

    Un equipo de albañiles de una obra, tiene que planificar la colocación de pisos. Dicha tarea se realiza 
    teniendo algunas consideraciones específicas, que tienen que ver con el corte de las baldosas, con el material 
    de pegado y la cantidad de trabajadores que hay en cada momento. En el arranque, el día uno (1), los albañiles 
    colocan siempre 100 baldosas. Luego, la cantidad que se coloca cada día se organiza de esta manera:

        Los días pares se colocan el doble de baldosas del día anterior.
        Los días impares (salvo el primer día) se coloca una cantidad igual a la suma de las que se colocaron los 2 dias anteriores.

    Implementar una función que permita saber la cantidad de baldosas que se colocan en total luego de transcurrida una determinada cantidad de días.

"""

def baldosasTotal(dias:int) -> int:
    baldosas = 0
    if dias == 0:
        return baldosas
    elif dias == 1:
        baldosas = baldosasTotal(dias-1) + 100
    elif dias % 2 == 0:
        baldosas += baldosasTotal(dias-1) * 2
    else:
        baldosas = baldosasTotal(dias-1) + baldosasTotal(dias-2)
    return baldosas

print(baldosasTotal(5))