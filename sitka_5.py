import csv
from datetime import datetime

open_file= open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=',')

header_row= next(csv_file)

counter= 0 
for x in header_row:
    if x == "TMIN":
        tmin=counter
    
    if x == "TMAX":
        tmax=counter
    
    counter +=1 

