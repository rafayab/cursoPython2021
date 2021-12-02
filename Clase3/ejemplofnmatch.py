import fnmatch
import os


# Busca todos los ficheros con el patron especificado
patron = 'clase*.py'
print('Patrón :', patron)
print('*****')

ficheros = os.listdir('./')
for nombre in ficheros:
    print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre, patron)))
    