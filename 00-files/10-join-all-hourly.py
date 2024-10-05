import os
import pandas as pd
import numpy as np

# Ruta de la carpeta donde están los CSVs diarios
folder_path = "research-data-hourly"
output_file = f"{folder_path}-all.csv"

# Umbrales para cada variable que quieres controlar
thresholds = {
    "TEMP": 45,  # Umbral para la temperatura
    "CO": 50,    # Umbral para el CO (puedes ajustarlo según tus necesidades)
}

# Lista para almacenar los DataFrames
df_list = []

# Recorrer todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        # Leer el archivo CSV y agregarlo a la lista de DataFrames
        df = pd.read_csv(file_path)
        
        # Iterar sobre cada variable umbralizada
        for variable, threshold in thresholds.items():
            if variable in df.columns:
                # Asegurar que la columna sea numérica
                df[variable] = pd.to_numeric(df[variable], errors="coerce")
                # Convertir a NaN los valores que excedan el umbral
                df.loc[df[variable] > threshold, variable] = np.nan
        
        df_list.append(df)

# Concatenar todos los DataFrames en uno solo
combined_df = pd.concat(df_list)

# Guardar el DataFrame combinado con los valores atípicos convertidos a NaN
combined_df.to_csv(output_file, index=False)

print("Done!")
