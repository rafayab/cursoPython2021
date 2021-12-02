# Un ejemplo creando un directorio en la carpeta inicio del usuario:
from pathlib import Path
import os

# Se obtiene el directorio inicio del usuario en SO Linux y Windows
fichero_path = Path(Path.home(), "directorio_ficheros")

# Si no existe el directorio, se crea
if not fichero_path.exists():
    os.makedirs(fichero_path)

# Se agrego el fichero al path
fichero_path = fichero_path.joinpath("quijote-ext03.txt")
# se escriben las siguientes líneas en el fichero
with fichero_path.open('w') as file:
    lineas = [
        "sdfdsfdasf daf asdf fsad sa dsa dsa d sad sd sd s ds ds "
        "dfsdfdsfsdf dfds fd fdfggh g  mmmmmmmmmmmmmmmmmmmmmm"
    ]
    file.writelines(lineas)


