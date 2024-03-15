numero = int(input("ingrese numero entero mayor a 3: "))
while(numero<=3):
    numero = int(input("numero no valido, ingrese nuevamente: "))
for i in range(1,numero+1):
    if(i%2!=0):
        print(i)