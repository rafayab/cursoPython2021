def funcion_excepciones():
    try:
        # Dividir entre 0 genera excepcion
        print(10 / 0)
    except ZeroDivisionError:
        print('Error. No se puede dividir por 0')
    else:
        # La excepcion no ha ocurrido
        print('La excepcion no ha ocurrido')
    finally:
        # Este bloque se ejecuta cuando todas las excepciones se han ejecutado')
        print('Finalizadas excepciones')

funcion_excepciones()
