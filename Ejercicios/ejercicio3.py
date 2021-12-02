# Ejercicio 3
# Escribir un programa que tome una lista de números (entre 5 y 10 números), haga
# una lista con el primero y el último de los elementos, otra con el valor máximo y mínimo, y
# por último las muestre en pantalla.

def ejercicio():
    entrada = input('Introduce una lista de numeros (entre 5 y 10):')
    lista = entrada.split(' ')
    if len(lista) >= 5 and len(lista) <= 10:
        lista1 = [lista[0], lista[-1]]
        lista2 = [min(lista), max(lista)]
        print('Lista 1 (Primero-Ultimo): ', lista1)
        print('Lista 2 (Min-Max): ', lista2)
        
    else:
        print('La lista debe ser de entre 5 y 10 numeros!')


ejercicio()
