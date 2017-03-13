#!/usr/bin/env

import folium

#geo_path = r'multi2.json'
geo_path = r'../parcels/tiny_geoJSON.json'
the_map = folium.Map([41.81, -87.70])
the_map.choropleth(geo_path=geo_path)

the_map.save("OSM_map.html")

