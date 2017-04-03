import json
neighbor_file = "/Users/galil/src/crime_mapper/lib/api/zoning/geoJSONs/tiny_even_neighbors.json"
score_dict = "/Users/galil/src/crime_mapper/zone_scores/zone_thefts_2016.json"
outfile = "/Users/galil/src/crime_mapper/zone_scores/filtered_thefts_2016.json"
with open(neighbor_file, "r") as f:
    data = json.load(f)
with open(score_dict, 'r') as f:
    scores =  json.load(f)
j_len = len(data["features"])
filtered_scores = {}
for i in range (0, j_len):
    curr_id = data["features"][i]["id"]
    tot_score = scores[str(curr_id)]
    neighbors = len(data["features"][i]["geometry"]["neighbors"])
    #import pdb; pdb.set_trace()
    for neighbor in data["features"][i]["geometry"]["neighbors"]:
        tot_score += scores[str(neighbor)]
    avg_score = tot_score / (neighbors + 1)
    filtered_scores[str(curr_id)] = avg_score
with open(outfile, "w") as f:
    json.dump(scores, f, sort_keys = True, indent = 4, ensure_ascii = False)
