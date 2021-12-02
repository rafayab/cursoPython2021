# Ejemplo de función
def multiplicar(x, y):
    return x * y

print(multiplicar(5,5))


# Ejemplo de funcion lambda
multiplicar = lambda x, y: x * y
print(multiplicar(5, 5))


# Ejemplo lambda dentro de una expresion - PEP 498
print(f'{(lambda x: x*5)(5)}')


