def valor_maximo(num1,num2,num3):
    maximo = num1
    if(num2>maximo):
        maximo = num2
    if(num3>maximo):
        maximo = num3
    return maximo

print(valor_maximo(1,2,3))
print(valor_maximo(2,3,1))
print(valor_maximo(3,2,1))