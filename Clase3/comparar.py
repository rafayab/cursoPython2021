import filecmp


# Directorios a comparar
dir1 = 'prueba'
dir2 = 'otraprueba'

# Ficheros comunes dentro de los directorios a comparar
comunes = ['quijote-ext01.txt']

# Comparar los metadatos de los ficheros comunes
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, comunes)

print("Verifica los metadatos:")
print("Coinciden:", match)
print("NO coinciden:", mismatch)
print("Errores:", errors, "\n")

# Compara también los datos dentro de los ficheros
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, comunes, shallow=False)

print("Deep comparison:")
print("Coinciden:", match)
print("NO coinciden:", mismatch)
print("Errores :", errors)
