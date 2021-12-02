import io
import shutil
import os


# Mover (o cambiar de nombre al fichero) al igual que el comando mv en GNU/Linux
# shutil.move(src='quijote-ext04.txt', dst='quijotetata.txt')

# Mover un fichero usando la biblioteca os
os.rename("quijotetata.txt", "quijotetataotro.txt")

# Borrar un fichero
os.remove("quijoteotro.txt")

