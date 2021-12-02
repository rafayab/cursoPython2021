# Ejercicio 2
# Preguntar al usuario un número y mostrar si es par o impar. Si el número es
# múltiplo de 4 imprimir el mensaje apropiado al usuario.

numero = input('Introduce un numero ')

if int(numero) % 2 == 0:
    print(f'{numero} es par')
else:
    print(f'{numero} es impar')

if int(numero) % 4 == 0:
    print(f'{numero} es multiplo de 4')

