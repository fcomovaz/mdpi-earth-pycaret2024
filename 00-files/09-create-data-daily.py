import pandas as pd
import numpy as np
import os
import warnings

warnings.filterwarnings("ignore")

# if research-data-daily doesn't exist, create it
if not os.path.exists("research-data-daily"):
    os.mkdir("research-data-daily")

stations = ["09_Estacion_Cruz_Roja", "10_Estacion_Nativitas", "11_Estacion_DIF"]
for station in stations:
    data = pd.read_csv(f"research-data-hourly/{station}.csv")
    data = data.groupby(["YEAR", "MONTH", "DAY"]).mean()
    data = data.drop(columns=["HOUR"])
    

    data.to_csv(f"research-data-daily/{station}.csv")

print("Done!")
