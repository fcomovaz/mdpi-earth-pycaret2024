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
                # Find the row with 'Hora' or 'HORA'
                for i, row in enumerate(rows):
                    if any("Mes" in cell or "MES" in cell for cell in row):
                        # Write the cleaned data to a  file
                        new_path = os.path.join(dirpath, f"{filename}")
                        with open(new_path, "w", newline="") as new_file:
                            writer = csv.writer(new_file)
                            writer.writerows(rows[i:])
                        break

print("Done!")
