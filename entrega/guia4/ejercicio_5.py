#retorna un string
def paridad(numero):
    if(numero%2==0):
        return f"{numero} es par"
    else:
        return f"{numero} es impar"

print(paridad(4))

#retorna un bool
def es_par(numero):
    return numero%2==0

print(es_par(3))
