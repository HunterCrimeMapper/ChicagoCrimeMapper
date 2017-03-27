#!/usr/bin/env

import folium

#geo_path = r'multi2.json'
geo_path = r'../api/zoning/geoJSONs/tiny_even_geoJSON.json'
the_map = folium.Map([41.81, -87.70])
#the_map = folium.map.FitBounds([(43.5, -88.5),(43.5, -86),(40.5, -86),(40.5, -88.5)])
the_map.choropleth(geo_path=geo_path)



the_map.save("/Users/galil/Documents/Hunter/Spring_2017/Capstone/CrimeMapper/mapper_src/src/ChicagoCrimeMapper/templates/new_html.html")

