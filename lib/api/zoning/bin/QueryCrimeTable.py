#---- Imports -----------------------------------------------------------------

from pandas.io.json import json_normalize

import pymysql.cursors
import pymysql
import json
import pandas as pd

#---- Public Classes ----------------------------------------------------------

class QueryCrimeTable(object):

    def __init__(self):
        self.size = 2675


    def get_crime_json(self, date_start, date_end, crime_type):

        connection = pymysql.connect(host='localhost',
                                     db = 'Chicago_Crimes',
                                     charset = 'utf8mb4',
                                     cursorclass = pymysql.cursors.DictCursor)

        data = []
        size = 2705
        iter_count = 1

        with connection.cursor() as cursor:
        	sql = ("SELECT zone, COUNT(id) FROM final_table "
        		"WHERE date >= '{}' AND date <= '{}' AND primary_type = '{}' AND NOT zone = 0 "
        		"GROUP by zone".format(date_start, date_end, crime_type))
        	cursor.execute(sql)
        	for row in cursor:
        		while iter_count < row['zone']:
        			data.append({"ID": iter_count, "value": 0.0})
        			iter_count += 1
        		data.append({"ID": row['zone'], "value": row['COUNT(id)']})
        		iter_count += 1

        while iter_count <= size:
        	data.append({"ID": iter_count, "value": 0.0})
        	iter_count += 1



        data_frame = json_normalize(data)
        boundaries = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
        percentiles = []
        for boundary in boundaries:
            percentiles.append(data_frame.quantile(boundary))

        percentile_data = {}
        for num in percentiles:
            percentile_data[num.name] = float(num.value)

        with open('/home/galil/src/ChicagoCrimeMapper/static/percentiles.json',
                   'w') as OF:
            json.dump(percentile_data, OF)

        with open('/home/galil/src/ChicagoCrimeMapper/static/data.json', 'w') as f:

            json.dump(data, f)
