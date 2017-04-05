import folium
import pandas as pd
import json

geo_path = r'/Users/galil/src/crime_mapper/lib/api/zoning/geoJSONs/tiny_broad_geoJSON.json'

zone_value = r'/Users/galil/src/crime_mapper/zone_scores/choro_smear_score.csv'


zone_data = pd.read_csv(zone_value)

crime_map = folium.Map(location=[41.889179863, -87.633110109],
                                max_zoom="15",
                                min_zoom="10")



crime_map.choropleth(geo_path=geo_path,
                     data = zone_data,
                     columns=['ID', 'value'],
	                 threshold_scale=[1, 2, 3, 4, 5, 6],
                     key_on ='feature.id',
	                 fill_color= 'YlOrRd',
                     fill_opacity=0.7,
                     line_opacity=0.2,
                     legend_name='CRIME IS BAD BABY',
                     highlight=True)

#import pdb;pdb.set_trace()
#folium.RegularPolygonMarker(location=[41.88, -87.6331],
#                         popup=str(zone_data.loc[1].value),
#                         fill_color=None, number_of_sides=3, radius=10).add_to(crime_map)

#with open(geo_path, 'r') as f:
#    geo_data = json.load(f)


#loc = geo_data['features'][1]['geometry']['coordinates'][0]
#folium.features.PolygonMarker(loc, popup="HelloChicago").add_to(crime_map)

#feature_group= folium.FeatureGroup(name='Zones')
#feature_group.layer_name='Zones'

#crime_map.add_child(feature_group)
#folium.LayerControl().add_to(crime_map)
crime_map.save(outfile ='../../templates/new_html.html')
