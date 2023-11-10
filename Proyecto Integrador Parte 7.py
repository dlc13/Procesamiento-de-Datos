import pandas as pd
import sys
import matplotlib.pyplot as plt

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

##Histogramas por Edad
data = pd.read_csv("datos_limpios.csv")
data['age'].plot(title='Distribución de Edades', kind='hist', edgecolor='black', xlabel='Edades', ylabel='Frecuencia')
plt.show()

##Histograma agrupado por Hombre y Mujer
dataAnemiaBySex = data[data["anaemia"] == 1].groupby("sex").size()
dataDiabetesBySex = data[data["diabetes"] == 1].groupby("sex").size()
dataFumadorBySex = data[data["smoking"] == 1].groupby("sex").size()
dataMuertoBySeX = data[data["DEATH_EVENT"] == 1].groupby("sex").size()
dataGroupedBySex = pd.DataFrame({"Anémicos": dataAnemiaBySex, "Diabeticos": dataDiabetesBySex,
                            "Fumadores": dataFumadorBySex, "Muertos": dataMuertoBySeX})
dataGroupedBySex.index = dataGroupedBySex.index.map({0: "Mujeres", 1: "Hombres"})
dataGroupedBySex = dataGroupedBySex.T
dataGroupedBySex.plot(title="Histograma Agrupado por Sexo" ,kind="bar", rot=0, ylabel="Cantidad", xlabel="Categorías")
plt.show()