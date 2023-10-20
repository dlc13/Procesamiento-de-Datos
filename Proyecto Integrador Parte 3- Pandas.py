import pandas as pd

df = pd.read_csv('heart_failure_clinical_records_dataset.csv', sep=',', header=0)

print(df.dtypes)
print(df.dropna())


cant_fumadores = df.groupby(['sex'])['smoking'].count()

print(cant_fumadores)
