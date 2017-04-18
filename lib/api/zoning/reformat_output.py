#!/usr/bin/python3

import csv
import json
import pandas as pd
import pprint



last_row = 2700
contents = []

with open('2017data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        contents.append(row)

data = pd.DataFrame.from_csv('2017data.csv')

max_value = float(data.max())
print(len(data.index))
if (len(data.index) == last_row - 1):
    print("Len data: {}, last_row -1: {}".format(len(data.index), last_row))
    min_value = float(data.min())

else:
    min_value = 0


with open('2017_theft.json', 'w') as outfile:
    outfile.write("[\n")
    i = 1
    for row in contents:
        #import pdb; pdb.set_trace()
        id = int(row[0])
        value = ((float(row[1]) - min_value)
                / (max_value - min_value)) * 100
        if (id  == i):
            outfile.write('{{"ID": {}, "value": {}}},\n' .format(i-1, value))
            i += 1
        else:
            while (i <= id):
                if (i == id):
                    outfile.write('{{"ID": {}, "value": {}}},\n'
                                                            .format(i-1, value))
                    i += 1
                else:
                    outfile.write('{{"ID": {}, "value": {}}},\n' .format(i-1, 0.0))
                    i += 1
    while (i <= last_row):
        outfile.write('{{"ID": {}, "value": {}}},\n'.format(i-1, 0.0))
        i += 1
    outfile.write("]")
