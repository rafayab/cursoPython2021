# Ejemplo simulando el constructor switch
def semana(i):
    dias={
            0:'Domingo',
            1:'Lunes',
            2:'Martes',
            3:'Miercoles',
            4:'Jueves',
            5:'Viernes',
            6:'Sabado'
    }
    return dias.get(i,'No corresponde a un dia de la semana')


print(semana(0))
print('***')
print(semana(10))
