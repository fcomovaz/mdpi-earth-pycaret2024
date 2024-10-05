import os
import pandas as pd
import numpy as np

root_dir = "Salamanca"
csv_extension = ".csv"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(csv_extension):
            old_path = os.path.join(dirpath, filename)
            # Read the CSV file into a DataFrame with specified encoding
            df = pd.read_csv(old_path, encoding="latin1", on_bad_lines="skip")
            # Replace 'NA' strings with np.nan
            df.replace("NA", np.nan, inplace=True)
            df.replace("NA ", np.nan, inplace=True)
            df.replace(" NA", np.nan, inplace=True)
            df.replace("#Â¡VALOR!", np.nan, inplace=True)
            df.replace("#¡VALOR!", np.nan, inplace=True)
            df.replace("#VALUE!", np.nan, inplace=True)
            df.replace("na", np.nan, inplace=True)
            df.replace("213,39", np.nan, inplace=True)
            df.replace("np.nan", np.nan, inplace=True)
            # Save the modified DataFrame back to the CSV file
            df.to_csv(old_path, index=False)

print("Done!")
