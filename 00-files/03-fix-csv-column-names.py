import os
import csv

# ['MES', 'DIA', 'HORA', 'O3 [ppm]', 'SO2 [ppm]', 'CO [ppm]', 'NO2 [ppm]', 'PM10 [µg/m3]', 'PM2.5 [µg/m3]', 'TEMP (°C)', 'WS (m/s)', 'WD (°)', 'HR (%)']



root_dir = "Salamanca"
csv_extension = ".csv"

# Diccionario para renombrar columnas
rename_dict = {
    "AÑO": "YEAR",
    "Año": "YEAR",
    "DIA": "DAY",
    "DÍA": "DAY",
    "Día": "DAY",
    "HORA": "HOUR",
    "Hora": "HOUR",
    "MES": "MONTH",
    "Mes": "MONTH",
    "UV": "RADSOL"
}

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(csv_extension):
            old_path = os.path.join(dirpath, filename)
            
            # Leer archivo CSV
            with open(old_path, "r", errors="ignore") as file:
                reader = csv.reader(file)
                rows = list(reader)
                
                # Asumimos que la primera fila contiene los nombres de columnas
                header = rows[0]

                # Renombrar columnas
                for i, column_name in enumerate(header):
                    # Renombrar según el diccionario
                    if column_name in rename_dict:
                        header[i] = rename_dict[column_name]

                    # Remover contenido entre brackets o paréntesis
                    if "[" in column_name or "(" in column_name:
                        header[i] = column_name.split("[")[0].split("(")[0].strip()

                    # Eliminar espacios en blanco
                    header[i] = header[i].replace(" ", "")

                # Guardar los cambios en un nuevo archivo
                new_path = os.path.join(dirpath, f"{filename}")
                with open(new_path, "w", newline="") as new_file:
                    writer = csv.writer(new_file)
                    # Escribir el header modificado y luego el resto de las filas
                    writer.writerow(header)
                    writer.writerows(rows[1:])

print("Done!")
