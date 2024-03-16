#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
#costo por hora. Después debe mostrar por pantalla el sueldo que le corresponde.
horas_trabajadas = int(input("Ingrese horas trabajadas: "))
costo_hora = float(input("Ingrese el costo por hora: "))
sueldo_diario = horas_trabajadas*costo_hora
print(F"Su sueldo por dia es {sueldo_diario}") 