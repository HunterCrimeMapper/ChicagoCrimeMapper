#!/usr/bin/env

#---- Imports -----------------------------------------------------------------
import json
import pprint

#---- Functions ---------------------------------------------------------------
def append_polygon_list(corners, polygon_list, id):
    new_square = {
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [corners]
                    },
                    "type": "Feature",
                    "id": (id + 1),
                    "properties": {}
                 }
    polygon_list.append(new_square)
    id += 1
    return [polygon_list, id]



def get_four_corners(start_long_lat, zone_size):
    if(isinstance(start_long_lat[1], str)):
        start_lat = float(start_long_lat[1].strip())
    else:
        start_lat = float(start_long_lat[1])
    if(isinstance(start_long_lat[0], str)):
        start_long = float(start_long_lat[0].strip())
    else:
        start_long = float(start_long_lat[0])

    NW = [start_long ,start_lat]
    NE = [start_long + zone_size[0], start_lat]
    SE = [NE[0], start_lat - zone_size[1]]
    SW = [NW[0], SE[1]]
    return [NW, NE, SE, SW]


def get_horizontal_zones(start_long_lat,
                         end_long,
                         zone_size,
                         polygon_list,
                         id):
    #horizontal_zones = []
    while(float(start_long_lat[0]) < float(end_long)):
        corners = get_four_corners(start_long_lat, zone_size)

        new_polygon_list, id = append_polygon_list(corners, polygon_list, id)
        start_long_lat = corners[1]
        list_and_id = [new_polygon_list, id]
    return list_and_id


def get_local_zone_size(start_lat,
                        end_lat,
                        zone_size):
    lat_delta = float(start_lat) - float(end_lat)
    #import pdb; pdb.set_trace()
    number_of_zones = int(lat_delta/(zone_size))
    difference = lat_delta%zone_size
    area = (zone_size * zone_size)
    print("difference : ", difference)
    print('number_of_zones : ', number_of_zones)
    if (number_of_zones != 0):
        delta = float(difference/number_of_zones)
        new_zone_height = zone_size + delta
        new_zone_length = area/new_zone_height
        if difference == 0:
            return [zone_size, zone_size]
    else:
        if difference == 0:
            return [zone_size, zone_size]
        new_zone_height = lat_delta
        new_zone_length = area/new_zone_height
    return [new_zone_length, new_zone_height]


def make_geoJSON(polygons):
    geo_JSON = {
            "type": "FeatureCollection",
            "features": polygons
            }
    return geo_JSON


def read_coordinates(file_name):
    file = []
    with open(file_name, "r") as f:
        for line in f:
            file.append(line)
    return file


def reverse_lat_long(lat_long):
    return [lat_long[1], lat_long[0]]


#---- Main --------------------------------------------------------------------

coordinates = read_coordinates("../coordinate_mapping/fourth_projection")
margin_of_insignificance = 0.00001
zone_size = 0.005
all_polygons = []
id = 0
i = 0
while i < len(coordinates):
    cur = coordinates[i]
    if (i != (len(coordinates) - 1)):
        next = coordinates[i + 1].split(',')
    ending_lat = next[0]
    polygons = []
    if('|' in cur):
        cur_sections = cur.split('|')
    else :
        cur_sections = [cur]
    for section in cur_sections:
        section_range = section.split('->')
        start = section_range[0].split(',')
        end = section_range[1].split(',')
        start_long_lat = reverse_lat_long(start)
        end_long_lat = reverse_lat_long(end)
        section_zones = []
        local_zone_size = get_local_zone_size(start_long_lat[1],
                                                    ending_lat,
                                                    zone_size)
        while(float(start_long_lat[1]) > float(ending_lat) + margin_of_insignificance):
            polygons, id = get_horizontal_zones(start_long_lat,
                                            end_long_lat[0],
                                            local_zone_size,
                                            polygons,
                                            id)
            start_long_lat = [float(start_long_lat[0]),
                              float(start_long_lat[1]) - local_zone_size[1]]


    for square in polygons:
        all_polygons.append(square)
    i += 1
    #the_final_file = make_geoJSON(polygons)
#pprint.pprint(all_polygons)
the_final_file = make_geoJSON(all_polygons)
pprint.pprint(the_final_file)
with open('../geoJSONs/tiny_broad_geoJSON.json', 'w') as outfile:
        json.dump(the_final_file, outfile)


