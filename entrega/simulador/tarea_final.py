import random

#Devuelve una lista con los resultados de un lanzamiento. 
#En el indice 0 se guarda el resultado total, en el indice N se muestra el valor del n-esimo dado lanzado
def lanzamiento(cantidad_dados, cantidad_caras): 
    resultados = list()
    suma = 0
    for i in range(cantidad_dados):
        resultados.append(random.randint(1,cantidad_caras))
        suma = suma+resultados[i]
    resultados.insert(0,suma)
    return resultados

#Muestra los valores de cada dado, seguido de la suma total de los valores.
def mostrar_resultados(resultados):
    i = 1
    while(i < len(resultados)):
        print(f"Resultado del dado {i} = {resultados[i]}")
        i = i+1
    print(f"Suma total = {resultados[0]}")

#Muestra numero de dados, numero de caras y resultado total de todos los lanzamientos realizados.
def mostrar_estadisticas(estadisticas):
    i = 0
    while(i<len(estadisticas)):
        print(f"Estadisticas del lanzamiento {i+1}: ")
        print(f"Numero de dados: {estadisticas[i][0]}")
        print(f"Numero de caras: {estadisticas[i][1]}")
        print(f"Resultado total: {estadisticas[i][2]}")
        i = i+1
    
    print()

def main():
    control = 1
    estadisticas = list()
    cantidad_dados = 1
    cantidad_caras = 6
    while(control != 0):
        print("0: salir")
        print(f"1: Seleccionar cantidad de dados (actual {cantidad_dados})")
        print(f"2: Seleccionar cantidad de caras (actual {cantidad_caras})")
        print("3: Mostrar estadisticas")
        print("4: Lanzar dados")
        control = int(input())
        match(control):
            case 1:
                cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar (entre 1 y 10): "))
                while(cantidad_dados<1 or cantidad_dados>10):
                    cantidad_dados = int(input("Cantidad no valida, ingrese nuevamente: "))
                print()
            case 2:
                print("1: Estandar")
                print("2: D4")
                print("3: D8")
                print("4: D10")
                print("5: D12")
                print("6: D120")
                cantidad_caras = int(input("Ingrese la cantidad de caras: "))
                match(cantidad_caras):
                    case 1:
                        cantidad_caras = 6
                    case 2: 
                        cantidad_caras = 4
                    case 3:
                        cantidad_caras = 8
                    case 4:
                        cantidad_caras = 10
                    case 5:
                        cantidad_caras = 12
                    case 6: 
                        cantidad_caras = 120
                    case _:
                        print("Opcion invalida. Se restauro el valor por defecto.")
                        cantidad_caras = 6

                print()
            case 3:
                mostrar_estadisticas(estadisticas)
                print()
            case 4:
                resultado = lanzamiento(cantidad_dados,cantidad_caras)
                mostrar_resultados(resultado)
                estadisticas.append([cantidad_dados, cantidad_caras, resultado[0]]) #Almacena numero de dados, numero de caras y el resultado total de cada lanzamiento realizado
                print()
    print("Gracias por jugar 😊")

main()