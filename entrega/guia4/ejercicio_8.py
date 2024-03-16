def invertir(cadena):
    nueva_cadena = ""
    for i in range(len(cadena)-1,-1,-1):
        nueva_cadena = nueva_cadena+cadena[i]
    return nueva_cadena

print(invertir("hola"))