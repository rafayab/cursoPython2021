class Empleado:
        def __init__(self, nombre, apellido, dni):
            self.nombre = nombre
            self.apellido = apellido
            self.dni = dni

class Aptitudes(Empleado):
    def __init__(self, nombre, apellido, dni, lenguaje, so, idiomas):
        Empleado().__init__(self, nombre, apellido, dni)
        self.lenguaje = lenguaje
        self.so = so
        self.idiomas = idiomas



