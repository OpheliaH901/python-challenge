# Modules
import os
import csv
import collections
from collections import Counter



#Set my variables
Votes_Count = 0
Total = 0
VoterID = 0


# A list of actors
Candidate_list = [
    "Correy" , "Khan", "Li", "O'Tooley"]

# Set path for file
csvpath = "Resources/election_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    # for row in csvreader:
    #     print(row)

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)


  #Read each row. Header not included. Loop counter through each row to give me total amount of votes
  
    for row in csvreader:
 #pull from collections module and assign so that total can be provided when we are reay to loop through data
        if list==row[2]:
            Votes_Count = Counter(list)  
            print(Votes_Count)


    
        


print("Election Results")
print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

#Exporting results to .txt file
results = open("ElectionDataResults.txt", "w")
results.write("Election Results" + '\n')
results.write("------------------------------------------" + '\n')
results.write(f"Total Votes : {Votes_Count}" + '\n')
results.write("------------------------------------------" + '\n')

results.close()