#!/usr/bin/env

import folium

#geo_path = r'multi2.json'
geo_path = r'../api/zoning/geoJSONs/JSON_with_borders.json'
the_map = folium.Map([41.81, -87.70])
the_map.choropleth(geo_path=geo_path)

the_map.save("/Users/galil/Documents/Hunter/Spring_2017/Capstone/CrimeMapper/mapper_src/templates/OSM_map.html")

