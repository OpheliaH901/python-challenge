# python-challenge
PyBank and PyPoll Challenges

PyBank 
We were tasked with analyzing a company's financial statements to come up with the following result:

The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The average of the changes in "Profit/Losses" over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period

A script was created to loop through the rows and determine each gain or loss that occured on a monthly basis (excluding the first month) and determining the average change amount, as well as the company's profits and losses and the times it occured.

PyPoll
This Python script would allow a small, rural town efficiently count votes during election season

With an imported .csv file, a script was created to count the number of votes for each candidate as well as the total. 
I was able to import collections module in python, which is a container that allows one to store data structures. I used the cadidates names to create a list. I wanted the script to loop through the rows of election_data.csv and give me a count for each candidate. From there, I could not only find the total amount of votes but also the percentages by using the percentage function to convert the amounts of votes received.