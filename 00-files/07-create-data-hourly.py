import os
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# define the root directory
root_dir = "Salamanca"
csv_extension = ".csv"
stations = ["09_Estacion_Cruz_Roja", "10_Estacion_Nativitas", "11_Estacion_DIF"]

# create research-data folder if it doesn't exist
if not os.path.exists("research-data-hourly"):
    os.mkdir("research-data-hourly")

cols = {
    "YEAR": int,
    "MONTH": int,
    "DAY": int,
    "HOUR": int,
    "O3": float,
    "SO2": float,
    "CO": float,
    "NO2": float,
    "PM2.5": float,
    "PM10": float,
    "WS": float,
    "WD": float,
    "TEMP": float,
    "HR": float,
    "PBAR": float,
    "RADSOL": float,
}

# subfolder = stations[2]
for subfolder in stations:
    df = pd.DataFrame(columns=cols)

    # read all csv files in the subfolder but in all levels
    for root, dirs, files in os.walk(os.path.join(root_dir, subfolder)):
        for file in files:
            if file.endswith(csv_extension):
                # read the csv file without specifying columns
                df_temp = pd.read_csv(os.path.join(root, file))
                # reindex to ensure all expected columns are present, filling missing columns with np.nan
                df_temp = df_temp.reindex(columns=cols, fill_value=np.nan)
                # append the DataFrame
                df = pd.concat([df, df_temp], ignore_index=True)



    # save the DataFrame to a csv file
    df.to_csv(os.path.join("research-data-hourly", subfolder+".csv"), index=False)


print("Done!")