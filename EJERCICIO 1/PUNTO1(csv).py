import pandas as pd

 

URL = "activaciones_samur_2022.csv"

 

# Leer CSV desde la URL

data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

 

print(data.head())  # Mostrar las primeras filas para visualizar los datos