# Ejemplo continue
for num in range(2, 10):
    if num % 2 == 0:
        print("Encontrado un numero par", num)
        continue
    # Con break sale de la iteración al encontrar el primer número par
    print("Encontrado un numero impar", num)
