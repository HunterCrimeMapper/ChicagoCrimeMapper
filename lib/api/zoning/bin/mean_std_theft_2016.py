#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

import json
import pandas as pd

#---- Main --------------------------------------------------------------------

infile = '/Users/galil/Documents/Hunter/Spring_2017/Capstone/src/zone_scores/zone_thefts_2016.json'

with open(infile, 'r') as f:
    data = json.load(f)

theft_data = pd.Series(data)

print(theft_data)

print(len(theft_data.index))

print("Mean: ", theft_data.mean())
print("Standard Deviation: ", theft_data.std())
