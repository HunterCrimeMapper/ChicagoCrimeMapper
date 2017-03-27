#! /usr/bin/python3 /usr/bin/env

#----- Imports ----------------------------------------------------------------

from ZoneChecker import ZoneChecker


#---- Main --------------------------------------------------------------------

geoJSON_file = "/Users/galil/Documents/Hunter/Spring_2017/Capstone/CrimeMapper/mapper_src/src/ChicagoCrimeMapper/tiny_even_geoJSON.json"

dict_file = "/Users/galil/Documents/Hunter/Spring_2017/Capstone/CrimeMapper/mapper_src/src/ChicagoCrimeMapper/section_dictionary.json"

zone_checker = ZoneChecker(geoJSON_file)
zone_checker.make_section_dictionary()
zone = zone_checker.get_zone_number((-87.675, 41.720))

print("That coordinate is in zone: ", zone)

zone_checker.save_section_dictionary(dict_file)
