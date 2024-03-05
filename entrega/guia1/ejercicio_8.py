# Se desea conocer el perímetro y el área de un rectángulo según su base y altura.
# Así mismo también se desean conocer los mismos datos para una circunferencia
# según su radio.
base = float(input("Base del rectangulo: "))
altura = float(input("Altura del rectangulo: "))

print(F"El perimetro del rectangulo es {base*2+altura*2}")

radio = float(input("Radio de la circunferencia: "))
pi = 3.1416
print(F"El perimetro de la circunferencia es {2*pi*radio}")