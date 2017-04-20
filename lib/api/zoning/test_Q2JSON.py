import json
import QueryToJSON as q2j

infile = '2017assault.csv'
outfile = '/Users/galil/src/crime_mapper/static/assault.json'

with open('/Users/galil/src/crime_mapper/static/crime_type2.json', 'w') as OF:
    data = {}
    data['url'] = '../static/homicide.json'
    json.dump(data, OF)

query = q2j.QueryToJSON(2704)

query.load_data_frame(infile)
query.make_percentile_map()
query.load_csv_into_json(infile, outfile)

