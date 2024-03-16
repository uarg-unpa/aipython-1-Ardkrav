numero = int(input('ingrese un numero natural: '))
suma = 0
while(numero<0):
    numero = int(input('numero ingresado no valido, ingrese nuevamente: '))
    
for i in range(1,numero+1):
    suma = suma + i
    print(i,end='')
    if(i!=numero):
        print(' + ',end='')
    else:
        print(' = ',end='')
print(suma)
