#Arman Sendag
#In Class Lab 2
#1-13-2025

#PROGRAM DESCRIPTION:
'''
The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room
can accommodate, and the number of people currently registered for the event. Write a program that
displays all rooms that are over the maximum limit of people and the number of people that have to
be notified that they will have to be put on the wait list. After the file is completely processed the
program should display the number of records processed and the number of rooms that are over the
limit.
'''


#VARIABLE DICTIONARY
#max_cap        the maximum room capacity, entered by the user
#people         the number of people attending the meeting, entered by the user
#diff           the difference between max capacity and people attending (diff = max_cap - people)
#name           the name of the meeting, entered by the user
#total_records  the total number of records processed from the csv file
#record         a single record from the csv file
#file           the csv file being read
#csvfile       the opened csv file object

#--------FUNCTIONS--------------------------------------------

#calculates the difference between max capacity and people attending
def difference(people, max_cap):
    diff = max_cap - people

    return diff #when diff < 0, means over capacity


#--------MAIN EXECUTING CODE--------------------------------

import csv

#welcome message
print("\n\n\tWelcome to my In-Class Lab 2!")


total_records = 0
roomsOver = 0 

#connecting to file
with open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/classLab2.csv") as csvfile:
    file = csv.reader(csvfile) 
    print("\n\nROOM                    MAX          MIN          OVER")
    for record in file:
        total_records += 1

        #gets information per roomsa
        name = record[0]
        max_cap = int(record[1])
        people = int(record[2])

        diff = difference(people, max_cap)

        #output results
        if diff < 0:
            roomsOver += 1
            print(f"{name:24}{max_cap:<13}{people:<13}{-diff}")

    print(f"\n\n\t\tTotal Records Processed: {total_records}")
    print(f"\t\tTotal Rooms Over Capacity: {roomsOver}")

#exit message
print("\n\n\tThank you for using the program. Goodbye.\n\n")