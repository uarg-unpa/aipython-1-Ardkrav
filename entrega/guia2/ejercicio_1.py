#Solicite información del usuario mediante el uso de input(“Ingrese su edad: ”). Si el
#usuario tiene 18 años o más, informar: tiene edad suficiente para conducir. Si tiene
#menos de 18 años,informe la cantidad de años que faltan.

edad = int(input("Ingrese su edad: "))
if(edad>=18):
    print("Tiene edad suficiente para conducir")
else:
    print(F"No tiene edad suficiente para condurcir. Le faltan: {18-edad} año(s)")