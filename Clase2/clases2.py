# Ejemplo de clase y creacion de una instancia de la misma
class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

    def festival_metodo(self):
        print('El mejor festival es: ')

# Se crea una instancia de la clase FestivalMusical
festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')

# Se accede al metodo
festival1.festival_metodo()

# Se accede a los atributos del objeto
print(festival1.nombre.upper())

festival1.nombre = ('Primavera Sound')
print(festival1.nombre)

# Eliminando el objeto
del festival1
print(festival1)


