class NombreDeLaClase:
    # Se utiliza la sentencia pass para evitar tener un error en una clase vacia
    pass

# Ejemplo de una clase y creacion de una instancia de la misma
class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        # Inicializa los parametros
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

# Se crea una instancia de la clase FestivalMusical
festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')

# Se accede a los atributos del objeto
print(festival1.nombre)

# Muestra la posicion del objeto de la clase FestivalMusical en la memoria
print(festival1)
