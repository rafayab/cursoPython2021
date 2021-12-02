import datetime
# Ejercicio 1
# Crear un programa que le pregunte al usuario su nombre y edad y le muestre el
# año en que cumplirá los 100 años.

nombre = input('Cual es tu nombre? ')
edad = int(input('Cual es tu edad? '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
anyo = date.strftime("%Y")

faltan = 100-edad
anyo_final = int(anyo)+faltan

print(nombre+" tienes "+str(edad) + " y cumpliras 100 años en "+str(anyo_final))
