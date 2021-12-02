from pathlib import Path
import os


# Lee del directorio superior
fichero_path = Path(os.pardir, "..", "quijote-ext01.txt")
with fichero_path.open('r') as file:
    print(file.read())
