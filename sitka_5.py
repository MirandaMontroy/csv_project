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
    
    if x == "DATE":
        date=counter

    counter +=1 

highs = []
dates = []
lows = []

for row in csv_file:
    try:
        high = (int(row[tmax]))
        low = (int(row[tmin]))
        converted_date = datetime.strptime(row[date],'%Y-%m-%d')

    except:
        print(f"Missing data for {converted_date}")
    
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)

#print(highs)

import matplotlib.pyplot as plt

fig= plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

#makes it label them diagonally to avoid overlap 
fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures in 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

plt.show()