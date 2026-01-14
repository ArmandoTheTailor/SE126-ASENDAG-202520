#Arman Sendag
#Lab 2
#1-13-2025

#PROGRAM DESCRIPTION:
'''
You have been asked to produce a report that lists all the computers in the csv file
filehandling.csv.
Your report should look like the following sample output.
The last line should print the number of computers in the file.
'''


#VARIABLE DICTIONARY
#computerType   the type of computer, from the csv file
#brand          the brand of the computer, from the csv file
#processor      the processor of the computer, from the csv file
#ram            the RAM size of the computer, from the csv file
#storage        the storage size of the computer, from the csv file
#numHardDrives  the number of hard drives of the computer, from the csv file
#secondDrive   the size of the second drive of the computer, from the csv file
#os             the operating system of the computer, from the csv file
#year           the year the computer was purchased, from the csv file
#total_records  the total number of records processed from the csv file
#record         a single record from the csv file
#file           the csv file being read
#csvfile       the opened csv file object

#--------FUNCTIONS--------------------------------------------



#--------MAIN EXECUTING CODE--------------------------------

import csv

#welcome message
print("\n\n\tWelcome to my Lab 2!")


total_records = 0

#connecting to file
with open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/filehandling.csv") as csvfile:
    file = csv.reader(csvfile) 
    print(f"\n\n{'TYPE':<15}{'BRAND':<15}{'PROCESSOR':<12}{'RAM':<10}{'STORAGE':<10}{'#DRIVES':<10}{'DRIVE2':<10}{'OS':<5}{'YEAR':<5}")
    for record in file:
        total_records += 1

        #gets information per computer

        type = record[0]

        #converts type code to full word
        if(type == "D"):
            type = "Desktop"
        elif(type == "L"):
            type = "Laptop"

        brand = record[1]
        
        #converts brand code to full word
        if(brand == "DL"):
            brand = "Dell"
        elif(brand == "HP"):
            brand = "HP"
        elif(brand == "GW"):
            brand = "Gateway"

        processor = record[2]
        ram = record[3]
        storage = record[4]
        numHardDrives = record[5]
        
        #checks if there is a second hard drive
        if(int(numHardDrives) == 2):
            secondDrive = record[6]
            os = record[7]
            year = record[8]
        else:
            secondDrive = ""
            os = record[6]
            year = record[7]
        

        #output results
        print(f"{type:<15}{brand:<15}{processor:<12}{ram:<10}{storage:<10}{numHardDrives:<10}{secondDrive:<10}{os:<5}{year:<5}")

    print(f"\n\n\t\tTotal Computers Processed: {total_records}")

#exit message
print("\n\n\tThank you for using the program. Goodbye.\n\n")