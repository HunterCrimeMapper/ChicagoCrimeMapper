import json

with open('2017_theft.json', 'r') as infile:
    data = json.load(infile)

with open('BEER.json', 'w') as outfile:
    json.dump(data, outfile)
