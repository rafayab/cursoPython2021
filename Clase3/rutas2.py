from pathlib import Path
import os


# Otros ejemplos leyendo de un directorio en la actual ruta, y de un directorio␣
#,superior:
# Lee del directorio "directorio1"
fichero_path = Path(".", "quijote-ext01.txt")
with fichero_path.open('r') as file:
    print(file.read())


