import io
import shutil


# Copiar ficheros situados en el mismo directorio
shutil.copy(src='quijote-ext01.txt', dst='quijoteotro.txt')

# Copiar ficheros preservando los metadatos
shutil.copy2(src="quijote-ext01.txt", dst="quijote-ext04.txt")

# Copiar al igual que el comando cp -R en GNU/Linux
shutil.copytree(src='prueba', dst='otraprueba')

# Ignorar ficheros .jpg al copiar
shutil.copytree(src='prueba', dst='otraprueba2', ignore= shutil.ignore_patterns('*.jpg'))
