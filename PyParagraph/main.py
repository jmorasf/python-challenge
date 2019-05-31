import os
import re

filePath = os.path.join('Resources', 'paragraph_1.txt')

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

with open(filePath) as txtFile:

    paragraph = txtFile.read()

txtFile.close()

words = paragraph.split()   #split paragraph by ' '
wordCount = len(words)      #number of words equals the size of the list
sentences = re.split("(?<=[.!?]) +", paragraph) #looking for dots (and a space?)
sentenceCount = len(sentences)                  #number of sentences equals the size of the list

#loop on words to get average length in letters
strTotal = 0
for i in range(len(words)):
    strTotal += len(words[i])
    
letterCount = strTotal/wordCount
sentenceLength = wordCount/sentenceCount

print ("Paragraph  Analysis")
print ("----------------------------")
print (f"Approximate Word Count: {wordCount}")  
print (f"Approximate Sentence Count: {sentenceCount}")
print (f"Average Letter Count: {'{:,.2f}'.format(letterCount)}")
print (f"Average Sentence Length: {'{:,.2f}'.format(sentenceLength)}")  

#creating a text file to print the results

txtpath = os.path.join('Resources', 'paragraph_results.txt')     
txtfile = open(txtpath,'w')

txtfile.write ("Paragraph  Analysis")
txtfile.write ("\n----------------------------")
txtfile.write ("\n" + paragraph)
txtfile.write ("\n----------------------------")
txtfile.write (f"\nApproximate Word Count: {wordCount}")  
txtfile.write (f"\nApproximate Sentence Count: {sentenceCount}")
txtfile.write (f"\nAverage Letter Count: {'{:,.2f}'.format(letterCount)}")
txtfile.write (f"\nAverage Sentence Length: {'{:,.2f}'.format(sentenceLength)}")
  
txtfile.close()
