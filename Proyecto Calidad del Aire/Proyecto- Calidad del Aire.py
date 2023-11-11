import pandas as pd
import requests
import sqlite3

# Importar Data
url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
data = pd.read_csv(url, sep=';')

# Concentración por ciudad
registros = []
cont = 1

def cargarRegistro(ciudad, concentraciones, contador):
    registro = {
        'city': ciudad,
        'overall_aqi': concentraciones['overall_aqi']
    }
    for key in concentraciones:
        if isinstance(concentraciones[key], dict) and 'concentration' in concentraciones[key]:
            registro[key] = concentraciones[key]['concentration']
    registros.append(registro)
    print(f'Registro numero {contador} añadido')

for ciudad, concentraciones in lista_datos:
    cargarRegistro(ciudad, concentraciones, cont)
    cont += 1

# Limpieza de datos
del data['Race']
del data['Count']
del data['Number of Veterans']
data.drop_duplicates(inplace=True)


# SQLite
con = sqlite3.connect('calidad_del_aire.db')
df_aqis = pd.read_sql_query("SELECT * FROM Concentrations", con)
data = pd.read_sql_query("SELECT * FROM Cities", con)

# Aplica un join entre las tablas "Cities" y "calidad_del_aire"
WITH joined_data AS (
 SELECT 
    Cities.City,  
    Cities.Total_Population, 
    AirQuality.overall_aqi
 FROM 
    Cities 
 JOIN 
    AirQuality 
 ON 
    Cities.ID = AirQuality.CityID
)





