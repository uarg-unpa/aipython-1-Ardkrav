def factorial(numero):
    factorial = 1
    for i in range(1,numero+1):
        factorial = factorial*i
    return factorial

print(factorial(5))