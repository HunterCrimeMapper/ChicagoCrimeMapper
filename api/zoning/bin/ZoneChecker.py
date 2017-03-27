#---- Imports -----------------------------------------------------------------

import json


#---- Public Classes ----------------------------------------------------------

class ZoneChecker(object):

    def __init__(self, geo_JSON_file, dict_file=None):
        self.file_location = geo_JSON_file
        if dict_file is not None:
            self.dictionary_of_sections = json.loads(dict_file)
        else:
            self.dictionary_of_sections = {}


    def get_sections(self):

        ##sections from projection lines
        sections = [42.022983,
                    42.019175,
                    42.012047,
                    41.995919,
                    41.978215,
                    41.968239,
                    41.960783,
                    41.937963,
                    41.934401,
                    41.916636,
                    41.908986,
                    41.901516,
                    41.896438,
                    41.884105,
                    41.868459,
                    41.829952,
                    41.822124,
                    41.816174,
                    41.805665,
                    41.800089,
                    41.782341,
                    41.774972,
                    41.764489,
                    41.762047,
                    41.713598,
                    41.706033,
                    41.670149,
                    41.663180,
                    41.656116,
                    41.644443]

        return sections



    def get_section_number(self, coordinate):
        sections = self.get_sections()
        for i in range(0, len(sections)):
            if (coordinate <= sections[i] and coordinate > sections[i+1]):
                return i


    def get_zone_number(self, crime_coordinates):
        section = self.get_section_number(crime_coordinates[1])
        for zone in self.dictionary_of_sections[section]:
            N_border = zone['geometry']['coordinates'][0][0][1]
            S_border = zone['geometry']['coordinates'][0][2][1]
            W_border = zone['geometry']['coordinates'][0][0][0]
            E_border = zone['geometry']['coordinates'][0][1][0]
            if (crime_coordinates[1] <= N_border and
                crime_coordinates[1] > S_border and
                crime_coordinates[0] >= W_border and
                crime_coordinates[0] < E_border):

                return zone


    def load_file(self):
        with open(self.file_location, "r") as f:
            data = json.load(f)

        return data


    def make_section_dictionary(self):
        data = self.load_file()
        j_len = len(data["features"])
        sec_len = len(self.get_sections())

        for i in range (0, j_len-1):
            curr_lat = data["features"][i]["geometry"]["coordinates"][0][0][1]
            curr_id =  data['features'][i]['id']
            sec_num = self.get_section_number(curr_lat)
            if sec_num not in self.dictionary_of_sections:
                self.dictionary_of_sections[sec_num] = list()
            self.dictionary_of_sections[sec_num].append(data['features'][i])


    def save_section_dictionary(self, outfile):
        with open(outfile, 'w') as f:
            json.dumps(self.dictionary_of_sections, f)


###your destionation here
#with open ("/Users/galil/Documents/Hunter/Spring_2017/Capstone/CrimeMapper/mapper_src/src/ChicagoCrimeMapper/sectioncheck.json", "w") as f:
#    json.dump(data, f, sort_keys = True, indent = 4, ensure_ascii = False)
