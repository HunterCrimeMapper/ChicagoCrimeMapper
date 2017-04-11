#!/usr/bin/python3 /usr/bin/env

import json
import csv
json_dict = {}
json_file = open('choro_score.json', 'w')
with open('choro_score.csv', 'r') as f:
    fields = ('ID','value')
    reader = csv.DictReader(f, fields)
    for line in reader:
        json.dump(line, json_file)
        json_file.write('\n')
