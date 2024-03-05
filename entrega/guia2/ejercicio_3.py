#Solicite al usuario una contraseña, utilizando input(“Ingrese su contraseña”),
#almacene esta contraseña en una variable. Luego informar si la contraseña
#introducida coincide con la guardada sin tener en cuenta mayúsculas y
#minúsculas
guardada = "contraseña"
contraseña = input("Ingrese la contraseña: ")

if(contraseña.lower() == guardada.lower()):
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
