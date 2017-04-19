import QueryToJSON as q2j


outfile = '/Users/galil/src/crime_mapper/static/crime_num_choro.json'
query = q2j.QueryToJSON(2704)

query.load_data_frame('2017data.csv')
query.make_percentile_map()
query.load_csv_into_json('2017data.csv', outfile)
