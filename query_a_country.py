import os

import numpy as np
import pandas as pd

df = pd.read_csv(os.getcwd() + "/city/output/list_of_countries.csv")
df.set_index("country", inplace=True)
print("Enter the name of a country : ", end=" ")
country_to_be_searched = input().title()

for i in df:
    if not np.isnan(df.loc[country_to_be_searched][str(i)]):
        print(i, df.loc[country_to_be_searched][str(i)])
