#Arman Sendag
#In Class Lab 3
#1-20-2025

#PROGRAM DESCRIPTION:
'''
Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.
'''


#VARIABLE DICTIONARY
# desktops - list to store desktops that need to be replaced
# laptops - list to store laptops that need to be replaced  
# numHardDrives - list to store number of hard drives per computer
# year - list to store the year of each computer
# laptopCost - cost to replace a laptop
# desktopCost - cost to replace a desktop
# numComputers - counter for number of computers processed
# type - variable to store type of computer being processed
# record - variable to store each record read from the csv file
# file - variable to store the csv file being read
# csvfile - variable to connect to the csv file

#--------FUNCTIONS--------------------------------------------



#--------MAIN EXECUTING CODE--------------------------------

#importing csv module
import csv

#welcome message
print("\n\n\tWelcome to my In Class Lab 3!")



desktops = [] 
laptops = []
numHardDrives = []
year = []
laptopCost = 1500
desktopCost = 2000
numComputers = 0

#connecting to file
with open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/filehandling.csv") as csvfile:
    file = csv.reader(csvfile) 
    for record in file:
        
        #gets information per computer

        type = record[0]

        

        numHardDrives.append(record[5])
        
        #checks if there is a second hard drive
        if(int(numHardDrives[numComputers]) == 2):
            year.append(record[8])
        else:
            year.append(record[7])
        

        #converts type code to full word and counts if it needs to be replaced
        if(type == "D"):
            if(year[numComputers] <= "16"):
                desktops.append(1)
        elif(type == "L"):
            if(year[numComputers] <= "16"):  
                laptops.append(1) 
        numComputers += 1
        
    #final output of total computers processed
    print(f"\n\n\t\tTo replace {len(desktops)} desktops it will cost ${len(desktops) * desktopCost : 5}")
    print(f"\t\tTo replace {len(laptops)} laptops it will cost  ${len(laptops) * laptopCost : 5}")

#exit message
print("\n\n\tThank you for using the program. Goodbye.\n\n")