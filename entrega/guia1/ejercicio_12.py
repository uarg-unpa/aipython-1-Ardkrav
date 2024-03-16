#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión
cantidad_invertir = float(input("Ingrese cantidad a invertir: "))
interes_anual = float(input("Ingrese interes anual: "))
anios = int(input("Ingrese el numero de años"))

print(F"El capital obtenido de la inversion es: {cantidad_invertir*(1+interes_anual/100)**anios}")