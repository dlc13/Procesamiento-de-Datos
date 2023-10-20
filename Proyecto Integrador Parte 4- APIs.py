import pandas as pd
import requests

def leer_url(url):
    get = requests.get(url)

    data = str(get.content)
    x = data.split('\\n')

    a = open('Datos.csv', 'wt')
    for linea in x:
        a.write(linea + '\n')
    a.close
leer_url('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')
df = pd.read_csv('Datos.csv', sep = ',', header = 0)
df = df.drop(len(df)-1)
print(df)