import QueryToJSON as q2j

query = q2j.QueryToJSON(2704)

query.load_data_frame('sample_output2.csv')
query.load_csv_into_json('sample_output2.csv')
query.export_to_JSON('test_it_outfile.json')

