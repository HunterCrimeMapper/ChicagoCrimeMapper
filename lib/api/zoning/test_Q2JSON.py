import QueryToJSON as q2j

query = q2j.QueryToJSON(2704)

query.load_data_frame('2017data.csv')
query.load_csv_into_json('2017data.csv', 'result_output.json')
