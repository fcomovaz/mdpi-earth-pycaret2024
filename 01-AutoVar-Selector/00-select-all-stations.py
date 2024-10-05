import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore
import os

stations = ["09_Estacion_Cruz_Roja", "10_Estacion_Nativitas", "11_Estacion_DIF"]
outputs = ["O3", "SO2", "CO", "NO2", "PM2.5", "PM10"]

if not os.path.exists("subsystems"):
    os.mkdir("subsystems")

def top_n_correlations(matriz_corr, variable, n=5):
    """
    Retorna un DataFrame con las top n correlaciones más altas para una variable específica.

    Parámetros:
    - matriz_corr (pd.DataFrame): Matriz de correlación.
    - variable (str): Nombre de la variable para la que deseas obtener las correlaciones.
    - n (int): Número de correlaciones más altas que se desean obtener.

    Retorna:
    - pd.DataFrame: DataFrame con las top n correlaciones más altas para la variable especificada.
    """
    # Extraer la fila/columna de correlaciones para la variable especificada
    correlaciones_variable = matriz_corr[variable].drop(
        variable
    )  # Elimina la autocorrelación

    # Ordenar por valor de correlación descendente
    corr_sorted = correlaciones_variable.abs().sort_values(ascending=False)

    # Obtener el top n correlaciones
    top_corr = corr_sorted.head(n)

    # Crear un DataFrame con las correlaciones y sus nombres
    df_corr = pd.DataFrame({"Variable": top_corr.index, "Correlación": top_corr.values})

    return df_corr


def threshold_correlation(matriz_corr, variable, umbral=0.2):
    """
    Retorna un DataFrame con todas las correlaciones superiores al umbral para una variable específica.

    Parámetros:
    - matriz_corr (pd.DataFrame): Matriz de correlación.
    - variable (str): Nombre de la variable para la que deseas obtener las correlaciones.
    - umbral (float): Valor umbral de correlación para filtrar.

    Retorna:
    - pd.DataFrame: DataFrame con las correlaciones que son superiores al umbral para la variable especificada.
    """
    # Extraer la fila/columna de correlaciones para la variable especificada
    correlaciones_variable = matriz_corr[variable].drop(
        variable
    )  # Elimina la autocorrelación

    # Filtrar por el umbral
    corr_filtered = correlaciones_variable[correlaciones_variable.abs() > umbral]

    # Ordenar por valor de correlación descendente
    corr_filtered = corr_filtered.abs().sort_values(ascending=False)

    # Crear un DataFrame con las correlaciones y sus nombres
    df_corr = pd.DataFrame(
        {
            "Variable": corr_filtered.index,
            "Correlación": corr_filtered.values,
        }
    )

    return df_corr

# time_window = ["hourly", "daily"]
time_window = ["daily"]

for tw in time_window:
    for variable in outputs:
        data = pd.read_csv(f"research-data-{tw}-all.csv")
        data_corr = np.abs(data.corr())
        threshold = 0.1

        # Obtener las correlaciones superiores a 0.2 para 'O3' en la matriz cr_corr
        corr_threshold = threshold_correlation(data_corr, variable, threshold)
        list_inputs = list(corr_threshold["Variable"])
        list_inputs = list_inputs + [variable]

        # print(f"All used inputs for {variable}")
        # print(list_inputs)
        data = data[list_inputs]
        # data = data.dropna()
        data.to_csv(f"subsystems/{variable}-all-joined-{tw}.csv", index=False)


print("Done!")