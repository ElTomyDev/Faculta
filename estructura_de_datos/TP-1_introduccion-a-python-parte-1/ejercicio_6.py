"""
Ejercicio 6:

    Escribir un programa que pregunte por el número de horas trabajadas y el costo por hora. 
    Después debe mostrar por pantalla el sueldo que corresponde.
    
"""
pedir_horas_trabajadas = int(input("¿Cuantas horas trabajaste?: "))
pedir_ganancia_en_hora = int(input("¿Cuanto ganas por hora?: "))

print(f"""
      Trabajaste {pedir_horas_trabajadas} horas y ganas ${pedir_ganancia_en_hora} por hora.
        - Total ganado: ${pedir_horas_trabajadas * pedir_ganancia_en_hora}
      """)