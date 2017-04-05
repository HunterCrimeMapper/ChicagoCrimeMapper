#---- Imports -----------------------------------------------------------------

import json


#---- Public Classes ----------------------------------------------------------

class BinarySearch(object):

    def __init__(self, geoJSON, number_of_zones):
        self.geoJSON = geoJSON
        self.start = 0
        self.end = number_of_zones
        self.middle_zone = number_of_zones // 2
        self.stuck = False
        self.found = False
        self.geoJSON = self.load_geoJSON(geoJSON)

    def bottom_of(self, zone):
        return self.geoJSON['features'][zone]['geometry']['coordinates'][0][2]

    def recurse(self, start, end):
        if (start == (end - 1) or start == end):
            print("One away")
            self.stuck = True
            self.middle_zone = start + 1
        self.start = start
        self.end = end
        self.middle_zone = start + ((end - start) // 2)


    def get_zone(self, long_lat):
        while not self.found:
            if self.stuck:
                return None
            #import pdb; pdb.set_trace()
            if long_lat[1] > self.top_of(self.middle_zone)[1]:
                self.recurse(self.start, self.middle_zone)
            elif long_lat[1] < self.bottom_of(self.middle_zone)[1]:
                print("made it deep")
                self.recurse(self.middle_zone, self.end)
            elif (long_lat[1] < self.top_of(self.middle_zone)[1] and
                  long_lat[1] > self.bottom_of(self.middle_zone)[1]):
                if long_lat[0] < self.top_of(self.middle_zone)[0]:
                    self.recurse(self.start, self.middle_zone)
                elif long_lat[0] > self.bottom_of(self.middle_zone)[0]:
                    self.recurse(self.middle_zone, self.end)
                elif (long_lat[0] > self.top_of(self.middle_zone)[0] and
                      long_lat[0] < self.bottom_of(self.middle_zone)[0]):
                    zone = self.geoJSON['features'][self.middle_zone]
                    self.found = True
                    return zone
                else:
                    return None
            else:
                return None


    def load_geoJSON(self, geoJSON):
        with open(geoJSON, 'r') as f:
            data = json.load(f)
            return data


    def top_of(self, zone):
        return self.geoJSON['features'][zone]['geometry']['coordinates'][0][0]

