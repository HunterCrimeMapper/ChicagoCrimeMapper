import json

##your infile here
#infile = "/Users/Mers/Desktop/Testing/tiny_even_neighbors.json"


#with open(infile, "r") as f:
#    self.data = json.load(f)
#---- Public Classes ----------------------------------------------------------

class BinarySearch(object):

    def __init__(self, data):
        self.data = data
        return


    def bin_search(self, lat, long):
        found = False
        start = 0
        #import pdb; pdb.set_trace()
        end = len(self.data["features"])
        while not found:
            curr = (end + start) // 2
            north = self.data\
                ["features"][curr]["geometry"]["coordinates"][0][0][1]
            if (lat > north):               ##CASE 1: too far north
                end = curr
            else:
                south = self.data\
                    ["features"][curr]["geometry"]["coordinates"][0][2][1]
                if (lat < south):           ##CASE 2: too far south
                    start = curr
                elif (lat >= south):
                    west = self.data\
                        ["features"][curr]["geometry"]["coordinates"][0][0][0]
                    east = self.data\
                        ["features"][curr]["geometry"]["coordinates"][0][1][0]
                    if (long < west):       ##CASE 3: too far west
                        end = curr
                    elif (long > east):     ##CASE 4: too far east
                        start = curr
                    else:                   ##otherwise, found it
                        print("found it!")
                        found = True

        return curr + 1
