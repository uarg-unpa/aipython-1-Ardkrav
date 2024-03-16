#aprovecho la funcion definida en el ejercicio 8
def invertir(cadena): 
    nueva_cadena = ""
    for i in range(len(cadena)-1,-1,-1):
        nueva_cadena = nueva_cadena+cadena[i]
    return nueva_cadena

def es_palindromo(cadena):
    if(cadena == invertir(cadena)):
        return True
    else:
        return False

print(es_palindromo("arenera"))
print(es_palindromo("arena"))