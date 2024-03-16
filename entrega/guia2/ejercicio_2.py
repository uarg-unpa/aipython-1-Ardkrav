#Compare su edad y mi edad usando if..else. ¿Quién es mayor (vos o yo)?,
#para el ingreso de la edad use input(“Ingrese su edad: ”)
#Use un condición anidada para:
#Imprimir año si la diferencia es de 1, sino años para diferencias
#mayores.
#Cuando las edades son iguales imprimir un mensaje personalizado,
#ser creativo

su_edad=int(input("Ingrese su edad: "))
mi_edad=int(input("Ingrese mi edad: "))

if(su_edad>mi_edad):
    if(su_edad-mi_edad==1):
        print("Usted es mayor por un año.")
    else:
        print(F"Usted es mayor por {su_edad-mi_edad} años")
elif(su_edad<mi_edad):
    if(mi_edad-su_edad==1):
        print("Yo soy mayor por un año.")
    else:
        print(F"Yo soy mayor por {mi_edad-su_edad} años")
else:
    print("Tenemos la misma edad.")
