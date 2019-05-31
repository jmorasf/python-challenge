import os
import csv
import locale

csvpath = os.path.join('Resources', 'election_data.csv')

#Initialize variables
totalVotes = 0 
candidates =  {}
thisName = ""


with open(csvpath, newline='') as csvfile:          #with csv file open

    csvreader = csv.reader(csvfile, delimiter=',')  #cursor on open file
    csv_header = next(csvreader)                    #skip first row

    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        thisName = row[2]
        if candidates.get(thisName) == None:        #assign value if this is the first time this candidate is found
            candidates[thisName] = 1
        else:
            candidates.update({thisName: candidates.get(thisName)+1})   #if candidate exists, add to the value already there
            

print ("Election Results")
print ("----------------------------")
print (f"Total Votes: {'{:,.0f}'.format(totalVotes)}")  
print ("----------------------------")

winner = ''
winnerTotal = 0

#only one loop needed to calculate percentages and determine the winner

for thisName in candidates:
    percentage = 100*candidates.get(thisName)/totalVotes
    if candidates.get(thisName) > winnerTotal:          #candidate with largest total wins             
        winner = thisName
        winnerTotal = candidates.get(thisName) 
    print (f"{thisName}: {'{:,.3f}'.format(percentage)}% ({'{:,.0f}'.format(candidates.get(thisName))})")  #results with proper number format

print ("----------------------------")
print (f"Winner: {winner}")  
print ("----------------------------")


#open a text file

txtpath = os.path.join('Resources', 'election_results.txt')     
txtfile = open(txtpath,'w')

txtfile.write ("Election Results")
txtfile.write ("\n----------------------------")
txtfile.write (f"\nTotal Votes: {'{:,.0f}'.format(totalVotes)}")  
txtfile.write ("\n----------------------------")

#same loop as before, but no calculation for winner needed

for thisName in candidates:
    percentage = 100*candidates.get(thisName)/totalVotes
    txtfile.write (f"\n{thisName}: {'{:,.3f}'.format(percentage)}% ({'{:,.0f}'.format(candidates.get(thisName))})")

txtfile.write ("\n----------------------------")
txtfile.write (f"\nWinner: {winner}")  
txtfile.write ("\n----------------------------")
