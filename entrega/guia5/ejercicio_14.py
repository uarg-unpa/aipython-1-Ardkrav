mi_lista = ['Boka','chan','ga','oshiette','kureta','ironna','mita','meni','narena','puninan','ndatte','dore','dore~']
nueva_lista = mi_lista[1:3]

def imprimir_lista(lista):
    for i in range(len(lista)):
        print(lista[i],"",end="")
    print()

imprimir_lista(mi_lista)
imprimir_lista(nueva_lista)