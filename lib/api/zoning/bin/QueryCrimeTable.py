#---- Imports -----------------------------------------------------------------

import pymysql.cursors
import pymysql


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
        size = 2675
        iter_count = 1

        with connection.cursor() as cursor:
        	sql = ("SELECT zone, COUNT(id) FROM filtered_2001_present "
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

        return data
