
#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

import csv
import json
import math

tally_file_path = '/Users/galil/src/crime_mapper/zone_scores/'



with open(tally_file_path + 'zone_thefts_2016.json', 'r') as f:
    data =  json.load(f)
