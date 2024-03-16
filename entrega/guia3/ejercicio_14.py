numero1 = int(input("Ingrese dos numeros: "))
numero2 = int(input())

if(numero1>numero2):
    aux = numero1
    numero1 = numero2
    numero2 = aux

if(numero1%2!=0): 
    numero1 = numero1-1 

for i in range(numero1+2,numero2,2): 
    print(i)