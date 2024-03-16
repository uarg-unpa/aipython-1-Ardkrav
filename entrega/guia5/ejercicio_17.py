def intercalar_listas(l1,l2):
    i = 0
    nueva_lista = []
    while(i<len(l1) and i<len(l2)):
        nueva_lista.append(l1[i])
        nueva_lista.append(l2[i])
        i = i+1
    while(i<len(l1)):
        nueva_lista.append(l1[i])
        i = i+1
    while(i<len(l2)):
        nueva_lista.append(l2[i])
        i = i+1
    return nueva_lista
    

lista1 = list("abcdefgh")
lista2 = list("12345")
nueva_lista = intercalar_listas(lista1,lista2)
print(lista1)
print(lista2)
print(nueva_lista)