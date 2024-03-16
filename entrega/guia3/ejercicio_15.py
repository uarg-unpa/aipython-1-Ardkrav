n = int(input("ingrese un numero entero: "))
es_primo = True

#todo numero es divisible por 1 y por si mismo (no se tienen en cuenta esos numeros)
#ningun numero n puede ser divisible por un numero mayor a n/2

#como el ejercicio solo pide saber si el numero es primo o no, se trata de buscar un solo numero 
#distinto de 1 y n que lo divida, si se encuentra termina el bucle
#se busca ese numero en el intervalo [2,n/2]

for i in range(2,int(n/2)+1): 
    if(n%i==0): 
        es_primo = False
        break
if(es_primo):
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")