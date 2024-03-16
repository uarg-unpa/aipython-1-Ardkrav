numero = int(input('ingrese un numero natural: '))
suma = 0
while(numero<0):
    numero = int(input('numero ingresado no valido, ingrese nuevamente: '))
    
for i in range(1,numero+1):
    print(i*2,end="")
    suma = suma+i*2
    if(i!=numero):
        print(" + ",end="")
print(f" = {suma}")