#Arman Sendag
#Lab 3
#1-20-2025

#PROGRAM DESCRIPTION:
'''
This lab is a continuation of the Voter Registration Lab from SE116.  The original prompt is as follows:

(Source: QBasic Fundamentals and Style, Quasney, Maniotes, Foremant; P. 190 #3)

Construct a program that will analyze potential voters. The program should generate the following totals:

Number of individuals not eligible to register.
Number of individuals who are old enough to vote but have not registered.
Number of individuals who are eligible to vote but did not vote.
Number of individuals who did vote.
Number of records processed.
 

Use this file to get your data: voters_202040.csv Download voters_202040.csv 

Remember: All string data being input to the program via a text or csv file is treated as string data

ID Number is 4 characters
Age is a number
Registered is either an N or a Y
Votes is either an N or a Y
 

Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.
'''


#VARIABLE DICTIONARY
#idNumbers      list of ID numbers from the csv file
#ages           list of ages from the csv file  
#registered     list of registration status from the csv file
#voted          list of voting status from the csv file
#notEligible    the total number of individuals not eligible to register
#notRegistered  the total number of individuals who are old enough to vote but have not registered
#didNotVote     the total number of individuals who are eligible to vote but did not vote
#didVote        the total number of individuals who did vote
#totalRecords   the total number of records processed

#--------FUNCTIONS--------------------------------------------



#--------MAIN EXECUTING CODE--------------------------------

#importing csv module
import csv

#welcome message
print("\n\n\tWelcome to my Lab 3!")

#initializing lists
idNumbers = []
ages = []
registered = []
voted = []

#initializing counters
notEligible = 0
notRegistered = 0
didNotVote = 0
didVote = 0


totalRecords = 0

#connecting to file
with open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile) 
    for record in file:
        totalRecords += 1

        #gets information per voter

        idNumbers.append(record[0])
        ages.append(int(record[1]))
        registered.append(record[2])
        voted.append(record[3])

    #processing lists to get totals
    for i in range(totalRecords):
        if(ages[i] < 18):
            notEligible += 1
        elif(registered[i] == "N"):
            notRegistered += 1
        elif(voted[i] == "N"):
            didNotVote += 1
        else:
            didVote += 1
                    

        
    #final output of total computers processed
    print(f"\n\n\t\tTotal number of individuals not eligible to register: {notEligible}")
    print(f"\t\tTotal number of individuals who are old enough to vote but have not registered: {notRegistered}")
    print(f"\t\tTotal number of individuals who are eligible to vote but did not vote: {didNotVote}")
    print(f"\t\tTotal number of individuals who did vote: {didVote}")
    print(f"\t\tTotal Voters Processed: {totalRecords}")

#exit message
print("\n\n\tThank you for using the program. Goodbye.\n\n")