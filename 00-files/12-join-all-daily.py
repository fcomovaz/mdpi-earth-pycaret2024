import os
import pandas as pd

# Ruta de la carpeta donde están los CSVs diarios
folder_path = "research-data-daily"
output_file = f"{folder_path}-all.csv"

# Lista para almacenar los DataFrames
df_list = []

# Recorrer todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        # Leer el archivo CSV y agregarlo a la lista de DataFrames
        df = pd.read_csv(file_path)
        df_list.append(df)

# Concatenar todos los DataFrames en uno solo
combined_df = pd.concat(df_list)

# Guardar el DataFrame combinado en un nuevo archivo CSV
combined_df.to_csv(output_file, index=False)

print("Done!")