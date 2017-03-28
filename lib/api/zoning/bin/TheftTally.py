#!/usr/bin/python3  /usr/bin/env

#---- Imports -----------------------------------------------------------------

from ZoneChecker import ZoneChecker

import pandas as pd

#---- Public Classes ----------------------------------------------------------

class TheftTally(object):

    def __init__(self):
        self.number_of_zones = 0
        self.zone_scores = {}


    def get_number_of_zones(self, geoJSON_file):
        with open(geoJSON_file, 'r') as f:
            data = json.load(f)
            self.number_of_zones = len(data['features'])
            for zone in range(0, self.number_of_zones):
                entry = {zone: 0}
                self.zone_scores.update({zone:0})

    def load_csv(self, infile):
        df = pd.read_csv(infile)
        return df


    def tally_crime_in_zone(self, df):
        pass
        #for crime in range (0, len(df.index)):

        #find zone
        #
