# Ejercicio 1
# Crear un programa que le pregunte al usuario su nombre y edad y le muestre el
# año en que cumplirá los 100 años.

nombre = input('Cual es tu nombre? ')
edad = input('Cual es tu edad? ')

anyo_final = 2021 + (100 - int(edad))
print(f'Cumpliras 100 años el {anyo_final}')
