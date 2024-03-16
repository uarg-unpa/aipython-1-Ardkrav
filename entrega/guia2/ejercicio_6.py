numero = int(input("Ingrese un numero entre 1-7: "))
if(numero>7 or numero<1):
    print("numero ingresado no valido.")
else:
    if(numero==1):
        print("Lunes")
    elif(numero==2):
        print("Martes")
    elif(numero==3):
        print("Miercoles")
    elif(numero==4):
        print("Jueves")
    elif(numero==5):
        print("Viernes")
    elif(numero==6):
        print("Sabado")
    else:
        print("Domingo")