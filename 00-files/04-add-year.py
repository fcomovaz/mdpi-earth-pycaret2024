import os
import csv
import numpy as np
import pandas as pd

# iterate over the root directory and the csv files, take the first row and check if there is YEAR in the first row
# if not, add a new column with the year, the year is calculated from the filename AA-MM-YY.csv
# the year needs to be YYYY
root_dir = "Salamanca"
csv_extension = ".csv"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(csv_extension):
            old_path = os.path.join(dirpath, filename)
            with open(old_path, "r", errors="ignore") as file:
                reader = csv.reader(file)
                rows = list(reader)
                if "YEAR" not in rows[0]:
                    year = filename.split("-")[2].split(".")[0]
                    year = f"20{year}"
                    rows[0].insert(0, "YEAR")
                    for i, row in enumerate(rows[1:]):
                        rows[i + 1].insert(0, year)
                    new_path = os.path.join(dirpath, f"{filename}")
                    with open(new_path, "w", newline="") as new_file:
                        writer = csv.writer(new_file)
                        writer.writerows(rows)

print("Done!")