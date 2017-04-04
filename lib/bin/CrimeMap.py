import folium
import pandas as pd


geo_path = r'/Users/galil/src/crime_mapper/lib/api/zoning/geoJSONs/tiny_even_geoJSON.json'

zone_value = r'/Users/galil/src/crime_mapper/zone_scores/choro_smear_score.csv'


zone_data = pd.read_csv(zone_value)

crime_map = folium.Map(location=[41.889179863, -87.633110109], max_zoom="15", min_zoom="10")



crime_map.choropleth(geo_path=geo_path, data = zone_data, columns=['ID', 'value'],

	threshold_scale=[1, 2, 3, 4, 5, 6], key_on ='feature.id',
	fill_color= 'YlOrRd', fill_opacity=0.7, line_opacity=0.2, legend_name='CRIME IS BAD BABY')

'''
crime_map.choropleth(geo_path=geo_path)

crime_map.add_child(folium.GeoJson(data=open('tiny_even_geoJSON.json'),
	name= "zones",
	style_function= lambda x: {'fill_color': '#de2d26' if x[]}
	))
'''



crime_map.add_child(folium.LayerControl())
crime_map.save(outfile ='../../templates/new_html.html')
