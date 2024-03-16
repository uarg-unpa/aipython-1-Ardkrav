#lista vacia
nombres=[]
#nombres=list()
#lista 
nombres=['agustin', 'pipi', 'emonuel']
#nombres=list(('agustin', 'pipi', 'emonuel'))

print(nombres)
#iterar
for i in range(len(nombres)):
    print(nombres[i])

#primer elemento
primer_elemento = nombres[0]
print(primer_elemento)

#agregar elemento al final
nombres.append("franco")
print(nombres)

#agregar elemento en una posicion de la lista
nombres.insert(0,"sandra")
print(nombres)

nombres[3]='algo'

for nombre in nombres:
    print(nombre)