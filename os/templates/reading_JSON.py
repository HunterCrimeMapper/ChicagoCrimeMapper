#!/usr/bin/python3

import pprint
import json


with open("test_geoJSON.json", "r") as f:
    data = json.load(f)



var = (data['features'][1]['geometry']['coordinates'])

search = -87.7
print(var)
for item in var:
    print(item)
    for num in item:
        print(num)
        if search in num:
            print("success")

#print("Here is the whole data:")
#pprint.pprint(data)
#
#print("Here is the first element of the value associated with the KEY 'features'")
#pprint.pprint( data['features'][0])
#
#print("Here is the SECOND element of the value associated with the KEY 'features'")
#pprint.pprint(data['features'][1])
