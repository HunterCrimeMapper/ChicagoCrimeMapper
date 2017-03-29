#!/usr/bin/python3 /usr/bin/env

#---- Imports -----------------------------------------------------------------

from TheftTally import TheftTally

import pandas as pd

#---- Main --------------------------------------------------------------------
crime_data = "/Users/galil/Documents/Hunter/Spring_2017/Capstone/Data/Crimes_THEFT_2016-Present.csv"

geoJSON_file = "/Users/galil/Documents/Hunter/Spring_2017/Capstone/CrimeMapper/mapper_src/src/ChicagoCrimeMapper/geoJSONs/tiny_even_geoJSON.json"

outfile = "/Users/galil/Documents/Hunter/Spring_2017/Capstone/CrimeMapper/mapper_src/src/ChicagoCrimeMapper/zone_thefts_2016.json"


theft_2016 =  TheftTally(geoJSON_file)
df = theft_2016.load_csv(crime_data)
theft_2016.tally_crime_in_zone(df)
#theft_2016.print_tally()
theft_2016.save_json(outfile)
