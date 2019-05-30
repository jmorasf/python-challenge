import os
import csv
import locale

locale.setlocale( locale.LC_ALL, '' )
csvpath = os.path.join('Resources', 'budget_data.csv')

def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

#Initialize variables
totalMonths = 0 
netProfit = 0
previousProfit = None
changes = 0
totalChanges = 0
greatestIncreaseMonth = "" 
greatestIncreaseAmount = 0  
greatestDecreaseMonth = "" 
greatestDecreaseAmount = 0  

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        totalMonths += 1
        profit = float(row[1])
        netProfit += profit
        if previousProfit != None:
            changes = profit - previousProfit
            totalChanges += changes
        previousProfit = profit  
        if changes > greatestIncreaseAmount:
            greatestIncreaseAmount = changes
            greatestIncreaseMonth = row[0]
        if changes < greatestDecreaseAmount:
            greatestDecreaseAmount = changes
            greatestDecreaseMonth = row[0]
       
averageChanges = totalChanges/(totalMonths-1)

txtpath = os.path.join('C:\Temp\PyBank\Resources', 'budget_results.txt')
txtfile = open(txtpath,'w')

print ("Financial Analysis")
print ("----------------------------")
print (f"Total Months: {totalMonths}")  
print (f"Total: {locale.currency(netProfit,grouping=True)}")
print (f"Average Change: {as_currency(averageChanges)}")   #print (f"Average Change: {locale.currency(averageChanges,grouping=True)}") (using locale library)
print (f"Greatest Increase in Profits: {greatestIncreaseMonth} {locale.currency(greatestIncreaseAmount,grouping=True)}")
print (f"Greatest Decrease in Profits: {greatestDecreaseMonth} {locale.currency(greatestDecreaseAmount,grouping=True)}")

txtpath = os.path.join('C:\Temp\PyBank\Resources', 'financial_data.txt')
txtfile = open(txtpath,'w')

txtfile.write ("Financial Analysis")
txtfile.write  ("\n----------------------------")
txtfile.write  (f"\nTotal Months: {totalMonths}")  
txtfile.write  (f"\nTotal: {locale.currency(netProfit,grouping=True)}")
txtfile.write  (f"\nAverage Change: {locale.currency(averageChanges,grouping=True)}")
txtfile.write  (f"\nGreatest Increase in Profits: {greatestIncreaseMonth} {locale.currency(greatestIncreaseAmount,grouping=True)}")
txtfile.write  (f"\nGreatest Decrease in Profits: {greatestDecreaseMonth} {locale.currency(greatestDecreaseAmount,grouping=True)}")
txtfile.close 
