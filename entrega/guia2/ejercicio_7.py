nota = int(input("Ingrese la nota: "))
if(nota>=80 and nota<=100):
    print("A")
elif(nota>=70 and nota<80):
    print("B")
elif(nota>=60 and nota<70):
    print("C")
elif(nota>=50 and nota<60):
    print("D")
elif(nota>=0 and nota<50):
    print("F")
else:
    print("Nota ingresada no valida.")