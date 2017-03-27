import json

##from border check
with open("C:\\Users\\Adnan\\Desktop\\capstone\\written.json", "r") as f:
    data = json.load(f)

##sections from projection lines
sections = [42.022983,
            42.019175,
            42.012047,
            41.995919,
            41.978215,
            41.968239,
            41.960783,
            41.937963,
            41.934401,
            41.916636,
            41.908986,
            41.901516,
            41.896438,
            41.884105,
            41.868459,
            41.829952,
            41.822124,
            41.816174,
            41.805665,
            41.800089,
            41.782341,
            41.774972,
            41.764489,
            41.762047,
            41.713598,
            41.706033,
            41.670149,
            41.663180,
            41.656116,
            41.644443]

j_len = len(data["features"])
sec_len = len(sections)

def get_section_number(coordinate):
    for i in range(0, sec_len):
        if (coordinate <= sections[i] and coordinate > sections[i+1]):
            return i


for i in range (0, j_len-1):
    curr_lat = data["features"][i]["geometry"]["coordinates"][0][0][1]
    sec_num = get_section_number(curr_lat)
    data["features"][i]["geometry"].update({"section": sec_num})

##your destionation here
with open ("C:\\Users\\Adnan\\Desktop\\capstone\\sectioncheck.json", "w") as f:
    json.dump(data, f, sort_keys = True, indent = 4, ensure_ascii = False)
