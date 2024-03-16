def cantidad_vacales(lista):
    cantidad = 0
    for i in lista:
        if(i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u'):
            cantidad = cantidad+1
    return cantidad

caracteres = list("Yo sOlo sE que no se nAda")
print(cantidad_vacales(caracteres))