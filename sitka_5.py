import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_lists(header_row, csv_file):

    counter= 0 
    for x in header_row:
        if x == "TMIN":
            tmin=counter
    
        if x == "TMAX":
            tmax=counter
    
        if x == "DATE":
            date=counter
        
        if x == "NAME":
            name=counter

        counter +=1
    

    highs = []
    dates = []
    lows = []

    for row in csv_file:
        try:
            high = (int(row[tmax]))
            low = (int(row[tmin]))
            converted_date = datetime.strptime(row[date],'%Y-%m-%d')
            title = row[name]

        except:
            print(f"Missing data for {converted_date}")
    
        else:
            highs.append(high)
            lows.append(low)
            dates.append(converted_date)

    return dates, highs, lows, title 

def main():
    open_file= open("sitka_weather_2018_simple.csv", "r")
    csv_file = csv.reader(open_file, delimiter=',')
    header_row= next(csv_file)

    open_file2= open("death_valley_2018_simple.csv", "r")
    csv_file2= csv.reader(open_file2, delimiter=',')
    header_row2= next(csv_file2)

    date1, high1, low1, title1 =get_lists(header_row, csv_file)
    date2, high2, low2, title2 =get_lists(header_row2, csv_file2)

    fig2, a = plt.subplots(2)

    fig2.suptitle(f"Temperature comparison between {title1} and {title2}")
    #fig2.autofmt_xdate()

    a[0].set_title(title1, fontsize=16)
    a[0].plot(date1, high1, c="red")
    a[0].plot(date1, low1, c="blue")
    a[0].fill_between(date1, high1, low1, facecolor='blue', alpha=0.1)
    a[0].set_xlabel("")

    a[1].set_title(title2, fontsize=16)
    a[1].plot(date2, high2, c="red")
    a[1].plot(date2, low2, c="blue")
    a[1].fill_between(date2, high2, low2, facecolor='blue', alpha=0.1)


    plt.xlabel("", fontsize=12)
    plt.ylabel("Temperature (F)", fontsize=12)
 #   plt.tick_params(axis="both", labelsize=12)

    plt.show()

'''
fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
'''
main()