# Modules
import os
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=',')

#     print(csvreader)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)

    

