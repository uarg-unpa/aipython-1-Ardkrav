print("Probando funcion"+" print()")
print("print()"*3)
print(10,3.14,"hola",False)

print()
edad = int(input("Ingrese edad: "))
print("su edad es:",edad)
print("su edad es:"+str(edad))
print(F"su edad es {edad}")

print()
num1 = 5
num2 = 9
print(F"{num1}+{num2}={num1+num2}")
print(F"{num1}-{num2}={num1-num2}")
print(F"{num1}*{num2}={num1*num2}")
print(F"{num1}%{num2}={num1%num2}")
print(F"{num1}/{num2}={num1/num2}")
print(F"{num1}//{num2}={num1//num2}")
print(F"{num1}**{num2}={num1**num2}")

print()
texto = "EStO eS uN TeXtO MeZcLaDo"
print(texto.title())
print(texto.upper())
print(texto.lower())
print(texto.replace("e","a"))
print(len(texto))