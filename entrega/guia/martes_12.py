num = int(input())
while num>0:
    if num%2==0:
        print("finalizacion del bucle")
        break
    num = int(input())

suma = 0
for i in range(0,30):
    print(i)
    if i>10:
        continue
    suma = suma+i
print(suma)

#def <nombre_funcion> ( <parametros> ):

def suma(num1,num2):
        return(num1+num2)

print(suma(1,2))
        