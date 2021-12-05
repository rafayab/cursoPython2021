import pandas as pd

# Se crea el dataframe
# Los datos han sido descargados de https://insights.stackoverflow.com/survey
# Pertenecen a la encuesta anual de desarrolladores año 2021
datos = pd.read_csv('survey_results_public.csv')

datos

# shape muestra la cantidad de filas y columnas del fichero en forma de tupla
datos.shape

# Muestra la información sobre el dataframe
datos.info()

# Muestra todas las columnas del fichero
pd.set_option('display.max_columns', 48)
pd.set_option('display.max_rows', 50)

# Se crea el schema del dataframe
schema_datos = pd.read_csv('survey_results_schema.csv')

schema_datos

# Muestra los 5 primeros registros del dataframe
datos.head()


# Muestra los últimos 10 registros
datos.tail(10)
