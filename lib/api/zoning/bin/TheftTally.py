#!/usr/bin/python3  /usr/bin/env

#---- Imports -----------------------------------------------------------------

from ZoneChecker import ZoneChecker
#from bin_search import BinarySearch
from bin_search_redux import BinarySearch

import json
import pandas as pd
import pprint

#---- Public Classes ----------------------------------------------------------

class TheftTally(object):

    def __init__(self, geoJSON_file):
        self.geoJSON_file = geoJSON_file
        self.zone_scores = {}
        self.number_of_zones = self.get_number_of_zones()
        self.data ={}


    def get_data_file(self):
        with open(self.geoJSON_file, 'r') as f:
            self.data = json.load(f)
            return


    def get_zone(self, long_lat):
        #zone_checker = ZoneChecker(self.geoJSON_file)
        #zone_checker.make_section_dictionary()
        #import pdb; pdb.set_trace()
        #zone = zone_checker.get_zone_number(long_lat)

        #zone_checker = BinarySearch(self.geoJSON_file, self.number_of_zones)
        #zone = zone_checker.bin_search(long_lat[1], long_lat[0])

        zone_checker = BinarySearch(self.geoJSON_file, self.number_of_zones)
        zone = zone_checker.get_zone(long_lat)
        return zone


    def get_number_of_zones(self):
        with open(self.geoJSON_file, 'r') as f:
            data = json.load(f)
            number_of_zones = len(data['features'])
            for zone in range(0, number_of_zones):
                entry = {zone: 0}
                self.zone_scores.update({zone:0})
            return number_of_zones


    def load_csv(self, infile):
        df = pd.read_csv(infile)
        self.get_number_of_zones()
        return df


    def print_tally(self):
        pprint.pprint(self.zone_scores)


    def save_json(self, outfile):
        with open(outfile, "w") as f:
            json.dump(self.zone_scores, f,
                       sort_keys=True, indent=4, separators=(',', ': '))


    def tally_crime_in_zone(self, df):
        self.get_data_file()
        for crime in range(0, len(df.index)):
            print("Crime out of 69080: ", crime)
            lat = df.loc[crime]['Latitude']
            long = df.loc[crime]['Longitude']
            long_lat = (long, lat)
            zone = self.get_zone(long_lat)
            #if (int(crime) == 96):
                #import pdb; pdb.set_trace()
            if zone is None:
                print("Long_lat {} is outside our geoJSON: ".format(long_lat))
            if zone is not None and zone is not -1:
                print("inside")
                tally = self.zone_scores[zone['id']]
                self.zone_scores.update({zone['id']: (tally + 1)})
                #tally = self.zone_scores[zone]
                #self.zone_scores[zone] = (tally + 1)
