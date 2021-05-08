# Modules
import os
import csv

# Set path for file
csvpath = "Resources/election_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    # for row in csvreader:
    #     print(row)

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)

     #Read each row. Header not included
    for row in csvreader:
