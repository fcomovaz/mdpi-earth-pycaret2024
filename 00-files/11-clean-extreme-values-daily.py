import pandas as pd
import numpy as np
import os
import warnings

warnings.filterwarnings("ignore")

# Si la carpeta 'research-data-daily' no existe, crearla
if not os.path.exists("research-data-daily"):
    os.mkdir("research-data-daily")

# Definir las estaciones
stations = ["09_Estacion_Cruz_Roja", "10_Estacion_Nativitas", "11_Estacion_DIF"]

# Umbrales para cada variable que quieres controlar
thresholds = {
    "TEMP": 45,  # Umbral para la temperatura
    "CO": 50,    # Umbral para el CO
}

for station in stations:
    # Cargar el archivo CSV correspondiente a cada estación
    data = pd.read_csv(f"research-data-hourly/{station}.csv")
    
    # Iterar sobre cada variable umbralizada
    for variable, threshold in thresholds.items():
        if variable in data.columns:
            # Convertir la columna a numérica
            data[variable] = pd.to_numeric(data[variable], errors="coerce")
            # Convertir a NaN los valores que excedan el umbral
            data.loc[data[variable] > threshold, variable] = np.nan

    # Agrupar por YEAR, MONTH, DAY y calcular la media de las demás columnas
    data = data.groupby(["YEAR", "MONTH", "DAY"]).mean()

    # Eliminar la columna 'HOUR' si existe
    if 'HOUR' in data.columns:
        data = data.drop(columns=["HOUR"])
    
    # Guardar el DataFrame limpio en la carpeta 'research-data-daily'
    data.to_csv(f"research-data-daily/{station}.csv", index=True)

print("Done!")
