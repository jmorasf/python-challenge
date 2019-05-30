import os
import csv
import locale

csvpath = os.path.join('Resources', 'election_data.csv')

#Initialize variables
totalVotes = 0 
candidates =  {}
thisName = ""


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        thisName = row[2]
        if candidates.get(thisName) == None:
            candidates[thisName] = 1
        else:
            candidates.update({thisName: candidates.get(thisName)+1})
            

print ("Election Results")
print ("----------------------------")
print (f"Total Votes: {'{:,.0f}'.format(totalVotes)}")  
print ("----------------------------")

winner = ''
winnerTotal = 0
for thisName in candidates:
    percentage = 100*candidates.get(thisName)/totalVotes
    if candidates.get(thisName) > winnerTotal:
        winner = thisName
        winnerTotal = candidates.get(thisName) 
    print (f"{thisName}: {'{:,.3f}'.format(percentage)}% ({'{:,.0f}'.format(candidates.get(thisName))})")

print ("----------------------------")
print (f"Winner: {winner}")  
print ("----------------------------")

txtpath = os.path.join('Resources', 'election_results.txt')
txtfile = open(txtpath,'w')

txtfile.write ("Election Results")
txtfile.write ("\n----------------------------")
txtfile.write (f"\nTotal Votes: {'{:,.0f}'.format(totalVotes)}")  
txtfile.write ("\n----------------------------")

for thisName in candidates:
    percentage = 100*candidates.get(thisName)/totalVotes
    txtfile.write (f"\n{thisName}: {'{:,.3f}'.format(percentage)}% ({'{:,.0f}'.format(candidates.get(thisName))})")

txtfile.write ("\n----------------------------")
txtfile.write (f"\nWinner: {winner}")  
txtfile.write ("\n----------------------------")
