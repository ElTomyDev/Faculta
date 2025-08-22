"""
Ejercicio 19

    Las y los alumnas y alumnos de un curso se han dividido en dos grupos A y B de acuerdo
    al género y el nombre. El grupo A esta formado por las personas de genero femenino con 
    una inicial de nombre anterior a la M y las personas de genero masculino con un inicial 
    de nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte 
    la inicial y el género, y muestre por pantalla el grupo que corresponde.
    
"""


def pertenece_al_grupo(inicial : str, genero : str):
    """
    Indica si el alumno con (inicial) y de (genero) pertenece al grupo
    A masculino o femeninp o al grupo B.
    """
    
    if inicial in "abcdefghijklm":
        return "Grupo A Femenino" if genero == "f" else "Grupo B"
    else:
        return "Grupo A Masculino" if genero == "m" else "Grupo B"
    

pedir_inicial = str(input("Dame una inicial: "))
pedir_genero = str(input("Dame un genero F o M: "))

print(f"""
La inicial '{pedir_inicial.upper()}' con genero '{pedir_genero.upper()}': pertenece al '{pertenece_al_grupo(pedir_inicial.lower(), pedir_genero.lower())}'
""")    
    

