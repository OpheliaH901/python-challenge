# Modules
import os
import csv

#Set my variables
Month = 0
ProfitLoss = 0
Great_Profit = 0
Great_Loss = 0


# Set path for file
csvpath = "Resources/budget_data.csv"

# with open(csvpath) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=',')

#     print(csvreader)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    # for row in csvreader:
    #     print(row)

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)

    #Read each row. Header not included
    for row in csvreader:
        Month +=1
        ProfitLoss+= int(row[1])
        if int(row[1]) > Great_Profit:
            Great_Profit = int(row[1])
            ProfitDate = row[0]
       
        if int(row[1]) < Great_Loss:
            Great_Loss = int(row[1])
            LossDate = row[0]

#   def average(numbers) will need for later:
#     length = len(numbers)
#     sum(numbers)
#     total = 0.0  

