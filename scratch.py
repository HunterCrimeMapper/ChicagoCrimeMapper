#!/usr/bin/env

with open("zone_score2.csv", 'w') as outfile:
    outfile.write("ID,value\n")
    for num in range(1, 450):
        outfile.write(str(num)+",0.0\n")
    for num in range(451, 900):
        outfile.write(str(num)+",1.0\n")
    for num in range(901, 1351):
        outfile.write(str(num)+",2.0\n")
    for num in range(1352, 1802):
        outfile.write(str(num)+",3.0\n")
    for num in range(1803, 2252):
        outfile.write(str(num)+",4.0\n")

    for num in range(2253, 2706):
        outfile.write(str(num)+",5.0\n")

