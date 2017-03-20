import folium
import pandas as pd


geo_path = r'tiny_even_geoJSON.json'
zone_value = r'zone_score.csv'

geo_path1 = r'geo_coord.json'
zone_value1 = r'zone_test.csv'

zone_data = pd.read_csv(zone_value)
zone_data1 = pd.read_csv(zone_value1)

def getColor(d):
	if d >= 6.0:
		color = '#de2d26'
	elif d >= 5.0:
		color = '#fc9272'
	elif d >= 4.0:
		color = '#9ecae1'
	elif d >= 3.0:
		color = '#a1d99b'
	elif d >= 2.0:
		color= '#f7fcb9'
	elif d >= 1.0:
		color= '#FFFFFF'
	return color


crime_map = folium.Map(location=[41.889179863, -87.633110109])

crime_map.choropleth(geo_path=geo_path, data = zone_data, columns=['ID', 'value'],
	threshold_scale=[1, 2, 3, 4, 5, 6], key_on ='feature.id',
	fill_color= 'BuPu', fill_opacity=0.7, line_opacity=0.2, legend_name='Zone Scores')

crime_map.choropleth(geo_path=geo_path1, data = zone_data1, columns=['ID', 'value'],
    threshold_scale=[1, 2, 3, 4, 5, 6], key_on ='feature.id',
    fill_color= 'BuPu', fill_opacity=0.7, line_opacity=0.2, legend_name='Zone Scores')

'''
crime_map.choropleth(geo_path=geo_path)

crime_map.add_child(folium.GeoJson(geo_path=geo_pathm, data=open('zone_score.csv'),
	name= "zones",
	style_function= lambda x: {'fill_color': '#de2d26' if 6 <= x['properties']['value'] else '#fc9272' if 5 <= x['properties']['value']}
	))
'''

html_str= """
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/jquery/1/jquery.min.js"></script>

    <!-- datepicker -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/momentjs/latest/moment.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/bootstrap/3/css/bootstrap.css" />
</head>
<body>
    <div class="container">
  <h2>Crime Mapper</h2>
  <p>Select the crime types you would like to see the data of.</p>
                                        
  
  <div class="dropdown">
    <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Crime Types
    <span class="caret"></span></button>
    <ul class="dropdown-menu">
    <li><a href="#" class="small" data-value="Arson" tabIndex="-1"><input type="checkbox"/>&nbsp;Arson</a></li>
    <li><a href="#" class="small" data-value="Assault" tabIndex="-1"><input type="checkbox"/>&nbsp;Assault</a></li>
    <li><a href="#" class="small" data-value="Battery" tabIndex="-1"><input type="checkbox"/>&nbsp;Battery</a></li>
    <li><a href="#" class="small" data-value="Burglary" tabIndex="-1"><input type="checkbox"/>&nbsp;Burglary</a></li>
    <li><a href="#" class="small" data-value="Concealed Carry License Violation" tabIndex="-1"><input type="checkbox"/>&nbsp;Concealed Carry License Violation</a></li>
    <li><a href="#" class="small" data-value="Criminal Sexual Assault" tabIndex="-1"><input type="checkbox"/>&nbsp;Criminal Sexual Assault</a></li>
    <li><a href="#" class="small" data-value="Criminal Damage" tabIndex="-1"><input type="checkbox"/>&nbsp;Criminal Damage</a></li>
    <li><a href="#" class="small" data-value="Criminal Trespass" tabIndex="-1"><input type="checkbox"/>&nbsp;Criminal Trespass</a></li>
    <li><a href="#" class="small" data-value="Deceptive Practice" tabIndex="-1"><input type="checkbox"/>&nbsp;Deceptive Practice</a></li>
    <li><a href="#" class="small" data-value="Domestic Violence" tabIndex="-1"><input type="checkbox"/>&nbsp;Domestic Violence</a></li>
    <li><a href="#" class="small" data-value="Gambling" tabIndex="-1"><input type="checkbox"/>&nbsp;Gambling</a></li>
    <li><a href="#" class="small" data-value="Homicide" tabIndex="-1"><input type="checkbox"/>&nbsp;Homicide</a></li>
    <li><a href="#" class="small" data-value="Human Trafficking" tabIndex="-1"><input type="checkbox"/>&nbsp;Human Trafficking</a></li>
    <li><a href="#" class="small" data-value="Interference With Public Officer" tabIndex="-1"><input type="checkbox"/>&nbsp;Interference With Public Officer</a></li>
    <li><a href="#" class="small" data-value="Intimidation" tabIndex="-1"><input type="checkbox"/>&nbsp;Intimidation</a></li>
    <li><a href="#" class="small" data-value="Kidnapping" tabIndex="-1"><input type="checkbox"/>&nbsp;Kidnapping</a></li>
    <li><a href="#" class="small" data-value="Liquor Law Violation" tabIndex="-1"><input type="checkbox"/>&nbsp;Liquor Law Violation</a></li>
    <li><a href="#" class="small" data-value="Motor Vehicle Theft" tabIndex="-1"><input type="checkbox"/>&nbsp;Motor Vehicle Theft</a></li>
    <li><a href="#" class="small" data-value="Narcotics" tabIndex="-1"><input type="checkbox"/>&nbsp;Narcotics</a></li>
    <li><a href="#" class="small" data-value="Non - Criminal" tabIndex="-1"><input type="checkbox"/>&nbsp;Non - Criminal</a></li>
    <li><a href="#" class="small" data-value="Non-Criminal" tabIndex="-1"><input type="checkbox"/>&nbsp;Non-Criminal</a></li>
    <li><a href="#" class="small" data-value="Non-Criminal (Subject Specified)" tabIndex="-1"><input type="checkbox"/>&nbsp;Non-Criminal (Subject Specified)</a></li>
    <li><a href="#" class="small" data-value="Obscenity" tabIndex="-1"><input type="checkbox"/>&nbsp;Obscenity</a></li>
    <li><a href="#" class="small" data-value="Offense Involving Children" tabIndex="-1"><input type="checkbox"/>&nbsp;Offense Involving Children</a></li>
    <li><a href="#" class="small" data-value="Other Narcotic Violation" tabIndex="-1"><input type="checkbox"/>&nbsp;Other Narcotic Violation</a></li>
    <li><a href="#" class="small" data-value="Other Offense" tabIndex="-1"><input type="checkbox"/>&nbsp;Other Offense</a></li>
    <li><a href="#" class="small" data-value="Prostitution" tabIndex="-1"><input type="checkbox"/>&nbsp;Prostitution</a></li>
    <li><a href="#" class="small" data-value="Public Indecency" tabIndex="-1"><input type="checkbox"/>&nbsp;Public Indecency</a></li>
    <li><a href="#" class="small" data-value="Public Peace Violation" tabIndex="-1"><input type="checkbox"/>&nbsp;Public Peace Violation</a></li>
    <li><a href="#" class="small" data-value="Ritualism" tabIndex="-1"><input type="checkbox"/>&nbsp;Ritualism</a></li>
    <li><a href="#" class="small" data-value="Robbery" tabIndex="-1"><input type="checkbox"/>&nbsp;Robbery</a></li>
    <li><a href="#" class="small" data-value="Sex Offense" tabIndex="-1"><input type="checkbox"/>&nbsp;Sex Offense</a></li>
    <li><a href="#" class="small" data-value="Stalking" tabIndex="-1"><input type="checkbox"/>&nbsp;Stalking</a></li>
    <li><a href="#" class="small" data-value="Theft" tabIndex="-1"><input type="checkbox"/>&nbsp;Theft</a></li>
    <li><a href="#" class="small" data-value="Weapons Violation" tabIndex="-1"><input type="checkbox"/>&nbsp;Weapons Violation</a></li>
    </ul>
  </div>
"""


iframe = folium.element.IFrame(html = html_str, width=300, height=200)
popup = folium.Popup(iframe, max_width=2650)


crime_map.add_child(folium.LayerControl())
folium.Marker([41.889179863, -87.633110109], popup=popup).add_to(crime_map)
crime_map.save(outfile ='./templates/map.html')
