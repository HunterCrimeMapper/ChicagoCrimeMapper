#!/usr/bin/python3

#---- Imports -----------------------------------------------------------------

import csv
import json
import pandas as pd
import pprint


#---- Classes -----------------------------------------------------------------

class QueryToJSON(object):


    def __init__(self, number_of_zones):
        self.json ={'list': []}
        self.max_value = 0.0
        self.number_of_zones = number_of_zones


    def export_to_JSON(self, outfile):
        with open(outfile, 'w') as of:
            json.dump(self.json,
                      of,
                      sort_keys = True,
                      indent =4,
                      ensure_ascii=False)


    def load_data_frame(self, infile):
        data = pd.DataFrame.from_csv(infile)
        self.max_value = float(data.max())

    def load_csv_into_json(self, infile, outfile):
        contents = []
        with open(infile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                contents.append(row)

        with open(outfile, 'w') as out:
            out.write("[\n")
            i = 1
            for row in contents:
#               import pdb; pdb.set_trace()
                id = int(row[0])
                value = float(row[1])#((float(row[1]) - 0)
                        #/ (self.max_value - 0)) * 100
                if (id  == i):
                    out.write('{{"ID": {}, "value": {}}},'.format(i, value))
                    i += 1
                else:
                    while (i <= id):
                        if (i == id):
                            out.write('{{"ID": {}, "value": {}}},'
                                                            .format(i, value))
                            i += 1
                        else:
                            out.write('{{"ID": {}, "value": 0.0}},'.format(i))
                            i += 1
            while (i <= self.number_of_zones):
                if (i == self.number_of_zones):
                    out.write('{{"ID":{}, "value": 0.0}}'.format(i))
                    i += 1
                else:
                    out.write('{{"ID": {}, "value": 0.0}},'.format(i))
                    i += 1
            out.write("]")
        with open(outfile, 'r') as IF:
            data = json.load(IF)

        with open('/Users/galil/src/crime_mapper/static/google_choro.json',
                   'w') as OF:
            json.dump(data, OF)

