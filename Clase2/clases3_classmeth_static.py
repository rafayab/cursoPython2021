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

@classmethod
def valor_ticket(cls, valor):
    cls.valor_ticket = valor

FestivalMusical.valor_ticket(50)

print(FestivalMusical.valor_ticket)  # Accede a la clase
print(festival1.valor_ticket)  # Accede a la instancia

# Confirmar si el evento es un dia de la semana o un fin de semana
@staticmethod
def dia_evento(dia):
    if dia.weekday() == 5 or dia.weekday() == 6:
        return print('es un final de semana')
    return print('es un dia laboral')

import datetime

dia1 = datetime.date(2021, 11, 9)
FestivalMusical.dia_evento(dia1)
