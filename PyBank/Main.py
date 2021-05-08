# Modules
import os
import csv

#Set my variables
Month = 0
ProfitLoss = 0
Great_Profit = 0
Great_Loss = 0
Change = 0

changelist = []
LastProfitLoss = 0
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
    csv_header = next(csvreader)

    #Read each row. Header not included
    for row in csvreader:
         #Average Change
         #month = 0, no change should be calculated
        # changelist = []
        # LastProfitLoss = 0

        if Month == 0:
            Change = 0
            LastProfitLoss = float(row[1]) 
            ProfitLoss = ProfitLoss + int(row[1])
            changelist.append(Change)
        else:
            Change = float(row[1]) - LastProfitLoss
            changelist.append(Change)
            LastProfitLoss=float(row[1])
            ProfitLoss = ProfitLoss + int(row[1])
        
        Month+=1
        # LastProfitLoss+= int(row[1])
        # if max(changelist) > Great_Profit:
        #     Great_Profit = Change
        #     ProfitDate = row[0]
       
        # if min(changelist) < Great_Loss:
        #     Great_Loss = Change
        #     LossDate = row[0]
          
print(changelist)     
print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months : {Month}")
print(f"Total: ${ProfitLoss}")
print(f"Average Change: {round(sum(changelist)/int(Month),2)} ")
print(f"Greatest Increase in Profits: (${max(changelist)})")
print(f"Greatest Decrease in Profits: (${min(changelist)})")

#Exporting results to .txt file
results = open("PyBankResults.txt", "w")
results.write("Financial Analysis" + '\n')
results.write("------------------------------------------" + '\n')
results.write(f"Total Months : {Month}" + '\n')
results.write(f"Total: ${ProfitLoss}" + '\n')
results.write(f"Average Change: {round(sum(changelist)/int(Month),2)} ")+ '\n')
results.write(f"Greatest Increase in Profits: Feb-2012 (${Great_Profit})" + '\n')
results.write(f"Greatest Decrease in Profits: Sep-2013 (${Great_Loss})" + '\n')
results.close()

#   def average(numbers) will need for later:
#     length = len(numbers)
#     sum(numbers)
#     total = 0.0  

