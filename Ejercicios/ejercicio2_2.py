
def ejercicio2():
    numero = input("Introduce un numero: ")
    numero = int(numero)
    if numero % 4 == 0:
        print("El numero ", numero, "es par ")
        print("El numero ", numero, "es multiplo de 4 ")
    elif numero % 2 == 0:
        print("El numero ", numero, "es par ")
    else:
        print("El numero ", numero, "es impar ")


ejercicio2()
