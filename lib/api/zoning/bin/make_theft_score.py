#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

import csv
import json
import math


#---- Functions ---------------------------------------------------------------

def get_log(num):
    num = math.log1p(num)
    return num



#---- Main --------------------------------------------------------------------





tally_file_path = '/Users/galil/src/crime_mapper/zone_scores/'



with open(tally_file_path + 'filtered_thefts_2016.json', 'r') as f:
    data =  json.load(f)

for line in range(1, len(data)):
    print("Before Zone: {}, Score: {}" .format(line, data[str(line)]))
    str_score = data[str(line)]
    score = get_log(float(str_score))
    data[str(line)] = score
    print("{},{}" .format(line, data[str(line)]))

with open(tally_file_path + 'choro_smear_score.csv', 'w') as outfile:
    outfile.write('ID,value\n')
    for line in (range(1, len(data))):

        outfile.write('{},{}\n'.format(line, data[str(line)]))

