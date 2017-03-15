import json

##your file location here
with open("C:\\Users\\Adnan\\Desktop\\capstone\\final_geoJSON.json", "r") as f:
    data = json.load(f)

lle = len(data["features"])

for i in range(0, lle):
    curr_id = data["features"][i]["id"]
    matches = []
    var = data["features"][i]["geometry"]["coordinates"][0]
    curr_north = var[0][1]
    curr_south = var[2][1]
    curr_west = var[0][0]
    curr_east = var[1][0]
    for x in range(0, lle):
        if x != i:
            var2 = data["features"][x]["geometry"]["coordinates"][0]
            temp_north = var2[0][1]
            temp_south = var2[2][1]
            temp_west = var2[0][0]
            temp_east = var2[1][0]
            ##if N/S or S/N border, or if E/W or W/E border w/ shared N or S
            if (curr_north == temp_south or curr_south == temp_north
                or curr_north == temp_north and (curr_east == temp_west or curr_west == temp_east)):
                ##if longitude between 
                if (temp_east >= curr_west and temp_east <= curr_east
                    or  temp_west >= curr_west and temp_west <= curr_east):
                    temp_id = data["features"][x]["id"]
                    if temp_id not in matches:
                        matches.append(temp_id)
    data["features"][i]["geometry"].update({"neighbors": matches})

##output file here
with open ("C:\\Users\\Adnan\\Desktop\\capstone\\bordernew.json", "w") as f:
    json.dump(data, f, sort_keys = True, indent = 4, ensure_ascii = False)
    
