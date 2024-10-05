import os
import csv

root_dir = "Salamanca"
csv_extension = ".csv"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(csv_extension):
            old_path = os.path.join(dirpath, filename)
            
            with open(old_path, "r", errors="ignore") as file:
                reader = csv.reader(file)
                rows = list(reader)

                # Extraer el mes del nombre del archivo
                month = filename.split("-")[1].split(".")[0]

                # Verificar si la columna "MONTH" ya existe
                if "MONTH" in rows[0]:
                    # Encontrar el índice de la columna "MONTH"
                    month_index = rows[0].index("MONTH")
                    # Sobrescribir la columna "MONTH" con el valor del mes
                    for i in range(1, len(rows)):
                        rows[i][month_index] = month
                else:
                    # Insertar la columna "MONTH" al principio
                    rows[0].insert(0, "MONTH")
                    for i in range(1, len(rows)):
                        rows[i].insert(0, month)
                
                # Guardar el archivo modificado
                new_path = os.path.join(dirpath, f"{filename}")
                with open(new_path, "w", newline="") as new_file:
                    writer = csv.writer(new_file)
                    writer.writerows(rows)

print("Done!")
