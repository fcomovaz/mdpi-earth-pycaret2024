import os
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")


# seasons per month spring-(3,4,5), summer-(6,7,8), autumn-(9,10,11), winter-(12,1,2)
def get_season(month):
    if month in [3, 4, 5]:
        return 0
    elif month in [6, 7, 8]:
        return 1
    elif month in [9, 10, 11]:
        return 2
    else:
        return 3
    

# read all the csv files in the directory research-data-hourly and add a column SEASON based on the MONTH column
for file in os.listdir('research-data-hourly'):
    if file.endswith('.csv'):
        df = pd.read_csv('research-data-hourly/' + file)
        df['SEASON'] = df['MONTH'].apply(get_season)
        df.to_csv('research-data-hourly/' + file, index=False)

print("Done!")


