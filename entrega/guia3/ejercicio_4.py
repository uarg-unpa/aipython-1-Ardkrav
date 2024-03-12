num1 = int(input("Ingrese dos numeros enteros: ")) 
num2 = int(input())

#Aseguro que num1<=num2 para que funcione el bucle
if(num1>num2):
    aux = num1
    num1 = num2
    num2 = aux

#Imprimo valores
aux = num1+1
while aux<num2:
    print(aux)
    aux = aux+1