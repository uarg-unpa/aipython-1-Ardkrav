#Para pagar un determinado impuesto se debe ser mayor de 18 años y tener ingresos
#iguales o superiores a $100000 mensuales. Escribir un programa que pregunte al
#usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
#que pagar o no el impuesto

edad = int(input("Ingrese su edad: "))
ingresos_mensuales = float("Ingrese sus ingresos mensules: ")
if(edad>18 and ingresos_mensuales>=100000):
    print("Debe pagar el impuesto.")
else:
    print("No debe pagar el impuesto.")