import sys
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from sklearn.manifold import TSNE
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score



csv = sys.argv[1]
df = pd.read_csv("Datos.csv")


##Valores Faltantes
valores_faltantes = df.isnull().any().any()
if valores_faltantes:
    print("Existen valores faltantes")
else:
    print("No existen valores faltantes")

##Filas Repetidas
duplicados = df.duplicated().sum()
if duplicados == 0:
    print("No hay registros duplicados")
else:
    print("Existen registros duplicados")

##Valores Atipicos
def eliminar_atipicos(df, columna):
    df_cleaned = df.copy()

    for X_columna in columna:
        q1 = df_cleaned[X_columna].quantile(0.25)
        q3 = df_cleaned[X_columna].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        df_cleaned = df_cleaned[(df_cleaned[X_columna] >= lower_bound) & (df_cleaned[X_columna] <= upper_bound)]

        # Verificar si la columna tiene solo valores binarios (1 y 0)
        conteo_valores = df_cleaned[X_columna].value_counts()
        if len(conteo_valores) == 2 and conteo_valores.sum() == len(df_cleaned):
            print(f"La columna {X_columna} no tiene valores atipicos")
        else:
            print(f"La columna {X_columna} tiene valores atipicos")



##categorizacion por Edades
def Edades_Categorizadas(edad):
    if edad <= 12:
        return "Niño"
    elif edad <= 19:
        return "Adolescente"
    elif edad <= 39:
        return "Joven adulto"
    elif edad <= 59:
        return "Adulto"
    else:
        return "Adulto mayor"

df["Edad"] = df["age"].apply(Edades_Categorizadas)
print("Edades_Categorizadas")

df.to_csv("./datos_limpios.csv", index=False)
print("Fin")

##Clasificación 1

data = pd.read_csv("datos_limpios.csv")
data = data.drop(columns=["Edades_Categorizadas"])
plt.figure()
grafico = data["DEATH_EVENT"].value_counts().plot(kind="bar", color=["red", "green"])
plt.title("Distribución de Fallecimientos")
plt.xlabel("Fallecimientos")
plt.ylabel("Frecuencia")
plt.xticks([0, 1], labels=["Vivos", "Fallecidos"])
plt.show()


entrenamiento = train_test_split(data.drop(columns=["DEATH_EVENT"]), data["DEATH_EVENT"], test_size=0.2, stratify=data["DEATH_EVENT"], random_state=42)
clf = DecisionTreeClassifier(max_depth=5, min_samples_split=60, random_state=42)
clf.fit(X_train, y_train)
y_predcit = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_predcit)
print(accuracy)