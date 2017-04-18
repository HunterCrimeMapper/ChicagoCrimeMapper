#!/usr/bin/python3

#---- Imports -----------------------------------------------------------------

import csv
import json
import pandas as pd
import pprint


#---- Classes -----------------------------------------------------------------

class QueryToJSON(object):


    def __init__(self, number_of_zones):
        self.json = []
        self.max_value = 0.0
        self.number_of_zones = number_of_zones


    def export_to_JSON(self, outfile):
        with open(outfile, 'w') as of:
            json.dump(self.json, of)


    def load_data_frame(self, infile):
        data = pd.DataFrame.from_csv(infile)
        self.max_value = float(data.max())

    def load_csv_into_json(self, infile):
        contents = []
        with open(infile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                contents.append(row)

        self.json.append("[n")
        i = 1
        for row in contents:
#            import pdb; pdb.set_trace()
            id = int(row[0])
            value = ((float(row[1]) - 0)
                    / (self.max_value - 0)) * 100
            if (id  == i):
                self.json.append('{{"ID": {}, "value": {}}},'
                                                        .format(i, value))
                i += 1
            else:
                while (i <= id):
                    if (i == id):
                        self.json.append('{{"ID": {}, "value": {}}},'
                                                        .format(i, value))
                        i += 1
                    else:
                        self.json.append('{{"ID": {}, "value": {}}},'
                                                        .format(i, 0.0))
                        i += 1
        while (i <= self.number_of_zones):
            self.json.append('{{"ID": {}, "value": {}}},'.format(i, 0.0))
            i += 1
        self.json.append("]")



#last_row = 2705
#contents = []
#
#with open('sample_output2.csv', 'r') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        contents.append(row)
#
#data = pd.DataFrame.from_csv('sample_output2.csv')
#
#max_value = float(data.max())
#print(len(data.index))
#if (len(data.index) == last_row - 1):
#    print("Len data: {}, last_row -1: {}".format(len(data.index), last_row))
#    min_value = float(data.min())
#
#else:
#    min_value = 0
#
#
#with open('formatted_scores.json', 'w') as outfile:
#    outfile.write("[\n")
#    i = 1
#    for row in contents:
#        #import pdb; pdb.set_trace()
#        id = int(row[0])
#        value = ((float(row[1]) - min_value)
#                / (max_value - min_value)) * 100
#        if (id  == i):
#            outfile.write('{{"ID": {}, "value": {}}},\n' .format(i, value))
#            i += 1
#        else:
#            while (i <= id):
#                if (i == id):
#                    outfile.write('{{"ID": {}, "value": {}}},\n'
#                                                            .format(i, value))
#                    i += 1
#                else:
#                    outfile.write('{{"ID": {}, "value": {}}},\n' .format(i, 0.0))
#                    i += 1
#    while (i <= last_row):
#        outfile.write('{{"ID": {}, "value": {}}},\n'.format(i, 0.0))
#        i += 1
#    outfile.write("]")
