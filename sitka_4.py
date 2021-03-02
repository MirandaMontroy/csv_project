import csv
from datetime import datetime
  
open_file= open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=',')

header_row= next(csv_file)

#enumerate returns both the index of each item and value of each item as you loop through list

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


highs = []
dates = []
lows = []

#example 

#mydate= "2018-07-01"
#converted_date = datetime.strptime(mydate, '%Y-%m-%d')
#print(converted_date)


for row in csv_file:
    try:
        high = (int(row[4]))
        low = (int(row[5]))
        converted_date = datetime.strptime(row[2],'%Y-%m-%d')

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


