from QueryCrimeTable import QueryCrimeTable


query = QueryCrimeTable()

data = query.get_crime_json('20160101', '20170101', 'Theft')

print(data)
