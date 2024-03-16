def promedio_lista(lista):
    suma = 0
    for i in lista:
        suma = suma+i
    return suma/len(lista)

lista = [10,10,5,9,1,2,3,6,6,1]
print(promedio_lista(lista))