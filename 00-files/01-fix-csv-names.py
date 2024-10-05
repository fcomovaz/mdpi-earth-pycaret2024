import os
import shutil

# iterate in the Salamanca folder and subfolders and rename the csv files
# each csv has the format AA_BB_CCC_DD_H.csv
# we want to rename them to AA-BB-DD.csv
root_dir = "Salamanca"
csv_extension = ".csv"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(csv_extension):
            parts = filename.split("_")
            new_filename = "-".join([parts[0], parts[1], parts[3], csv_extension])
            old_path = os.path.join(dirpath, filename)
            new_path = os.path.join(dirpath, new_filename)
            # print("Renaming:", old_path, "to", new_path)
            os.rename(old_path, new_path)
            # print("Renamed:", old_path, "to", new_path)

print("Done!")
