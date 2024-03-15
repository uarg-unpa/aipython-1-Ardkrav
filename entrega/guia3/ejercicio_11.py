numero=int(input('ingrese un numero: '))
for i in range(1,numero+1):
    if(i%2!=0):
        for j in range(i,0,-1):
            if(j%2!=0):
                print(j,'',end='')
        print()
