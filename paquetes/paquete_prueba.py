from paquete import modulo1, modulo2


llamar_modulo = modulo1.Clase1('Clase1')   # Crear la instancia
print(llamar_modulo)       # Direccion del objeto en memoria
print(modulo1.Clase1.mostrar)    # Direccion de la clase

print(llamar_modulo.mostrar())


llamar_modulo2 = modulo2.Clase2('Pepe')
llamar_modulo2.mostrar()


