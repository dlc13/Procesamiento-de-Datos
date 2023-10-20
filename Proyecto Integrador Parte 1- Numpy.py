from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

lista_edad = data["age"]
edad_Array = np.array(lista_edad)

edadPromedio = int(round(np.average(edad_Array)))
print(edadPromedio)
print(dataset)