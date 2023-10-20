import pandas as pd

df = pd.read_csv('heart_failure_clinical_records_dataset.csv', sep=',', header=0)

vivos = df[df['DEATH_EVENT'] == 0]
muertos = df[df['DEATH_EVENT'] == 1]

edadPromedioVivos = int(round(vivos["age"].mean()))
edadPromedioMuertos = int(round(muertos["age"].mean()))

print(edadPromedioVivos)
print(edadPromedioMuertos)