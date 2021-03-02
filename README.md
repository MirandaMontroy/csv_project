# matplotlib_csv
Advanced Python - Matplotlib - using CSV files

This project follows along with class for sitka1-4, with sitka-5 being independent work 

Overall, this project walks through the steps of using matplotlib with increasing complexity. 

Sitka_1: uses the ennumerate function to get an idea of how the data is laid out in the monthly file, 
uses that information to create a list of temperature highs read in from the file, and then 
plots that list using matplotlib. 

Sitka_2: all of sitka_1 with the addition of reading in dates and reformatting them, then saving 
them into a list. The program then plots high temperatures as a function of dates, using formatting 
to make the x-axis readable. 

Sitka_3: all of sitka_2 with the addition of a lows list, created the same way as highs, and plotted 
on the same graph as a function of dates. The yearly sitka csv file is used for this program. Then the area between the highs and lows was shadded in as a light blue. A brief example of subplotting follows, with the top graph plotting only highs and the bottom graph plotting only lows.

Sitka_4: all of sitka_3 but adds error handling and uses the death valley csv file, so the program no longer crashes when it attempts to read in data that is not there. The error handling is a try/except/else statement that prints out the string "missing data" and the date for whatever date information is missing for. This program is also an introduction to fstrings, a type of string output formatting. 

Sitka_5: This was done independently but also includes all of sitka_4, but repurposes it so that the code that creates the lists containing the highs/lows/dates is a function. The program also plots the yearly highs and lows as a function of date and shades the area in between the highs and lows for sitka and death valley on two seperate subplots. This program does not use ennumerate to find the indexes of the information in the file but uses a for loop that will find and assign the proper values, meaning that either file can be put through the function and get the proper indexes assigned. 

sitka_weather_07-2018_simple.csv: This file contains the data used in the early sitka examples and only contains data for July 2018

sitka_weather_2018_simple.csv: This file contains the yearly data for the sitka station 

death_valley_2018_simple.csv: This file contains the yearly data for the death valley station 
