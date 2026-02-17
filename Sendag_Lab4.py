#Arman Sendag
#Lab 4
#1-27-2025

#PROGRAM DESCRIPTION:
'''
Part 1

Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.

Original File Headers

FIELD0             FIELD1            FIELD2       FIELD3        FIELD4     

Firstname          Lastname        Test1         Test2             Test3

 

Part 2

Next, reprocess the lists to find each student's current average score, letter grade equivalent, and the class average. 

While processing in the for loop, store each student's average into a new list called 'num_avg' and their letter grade into a list called 'let_avg'. Then, print each student's full information, record by record, including average score and average letter equivalent.  After this print of the original file data from the lists, write each student's data into a new file called compiled_class_info.csv. Once complete, print to the console the total number of student's in the class along with the class numeric average to the console for the user.  

 

Processed Parallel List Headers

FIELD0             FIELD1            FIELD2       FIELD3        FIELD4     FIELD5      FIELD6

firstName          lastName        test1         test2             test3       num_avg   let_avg

 

Part 3

After your final display using the 1D parallel lists, create a sequential search program which allows the user to repeatedly utilize the following menu of search types. When a searched for item is found, display all student data to the console. When a search is compete and no matching data is found, alert the user. Search options 1 and 2 should only show one found student, where search option 3 should show a potential of multiple students.

 

Search Menu

1. Search by LAST name 

2. Search by FIRST name

3. Search by LETTER GRADE

4. Exit
'''


#VARIABLE DICTIONARY


#--------FUNCTIONS--------------------------------------------

#function to determine letter grade based on numeric avg score
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#--------MAIN EXECUTING CODE--------------------------------

#importing csv module
import csv

#welcome message
print("\n\n\tWelcome to my Lab 4!")

#initializing lists
firstNames = []
lastNames = []
test1Scores = []
test2Scores = []
test3Scores = []
avgScores = []
letterGrades = []

#initializing other variables
index = 0



#connecting to file
with open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/class_grades-2.csv") as csvfile:
    file = csv.reader(csvfile) 
    for record in file:
        #appends each field to respective list
        firstNames.append(record[0])
        lastNames.append(record[1])
        test1Scores.append(int(record[2]))
        test2Scores.append(int(record[3]))
        test3Scores.append(int(record[4]))
#disconnects from file

for i in range(len(firstNames)):
    #calculates avg score and letter grade for each student and appends to respective lists
    avgScores.append((test1Scores[i] + test2Scores[i] + test3Scores[i]) / 3)
    letterGrades.append(grade(avgScores[i]))

#creates a header for the output
print ("\n\n\tStudent Records:\n")
print(f"{'First Name':<15}{'Last Name':<15}{'Test1':<10}{'Test2':<10}{'Test3':<10}{'Avg Score':<12}{'Letter Grade':<15}")
print("-" * 87)
#prints each student's full information
for i in range(len(firstNames)):
    print(f"{firstNames[i]:<15}{lastNames[i]:<15}{test1Scores[i]:<10}{test2Scores[i]:<10}{test3Scores[i]:<10}{avgScores[i]:<12.2f}{letterGrades[i]:<15}") 
print("-" * 87)
print("\n\n\tTotal Students:", len(firstNames))  

#write data to new csv file
file = open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/compiled_class_info.csv", "w")
for i in range (len(firstNames)):
    file.write(f"{firstNames[i]},{lastNames[i]},{test1Scores[i]},{test2Scores[i]},{test3Scores[i]},{avgScores[i]:.2f},{letterGrades[i]}\n")
file.close()

#sequential search menu
print("\n\n\tWelcome to Student Search Menu")
answer = input("\nWould you like to search for a student? (y/n): ").lower()
while(answer == "y"):
    print("\n\n\tSearch Menu:")
    print("\n1. Search by LAST name")
    print("2. Search by FIRST name")
    print("3. Search by LETTER GRADE")
    print("4. Exit")

    searchOption = input("\nPlease enter the number of your search option: ")

    #last name search
    if(searchOption == "1"):
        lastNameSearch = input("\nEnter the LAST name of the student you are searching for: ")
        found = -1
        for i in range(len(lastNames)):
            if(lastNames[i].lower() == lastNameSearch.lower()):
                found = i
        if(found != -1):
            print(f"\nStudent Found:\n{firstNames[found]} {lastNames[found]}, Test1: {test1Scores[found]}, Test2: {test2Scores[found]}, Test3: {test3Scores[found]}, Avg Score: {avgScores[found]:.2f}, Letter Grade: {letterGrades[found]}")
        else:
            print("\nNo student found with the last name: ", lastNameSearch)
    
    #first name search
    elif(searchOption == "2"):
        firstNameSearch = input("\nEnter the FIRST name of the student you are searching for: ")
        found = -1
        for i in range(len(firstNames)):
            if(firstNames[i].lower() == firstNameSearch.lower()):
                found = i
        if(found != -1):
            print(f"\nStudent Found:\n{firstNames[found]} {lastNames[found]}, Test1: {test1Scores[found]}, Test2: {test2Scores[found]}, Test3: {test3Scores[found]}, Avg Score: {avgScores[found]:.2f}, Letter Grade: {letterGrades[found]}")
        else:
            print("\nNo student found with the first name: ", firstNameSearch)

    #letter grade search
    elif(searchOption == "3"):
        letterGradeSearch = input("\nEnter the LETTER GRADE you are searching for: ").upper()
        foundStudents = []
        for i in range(len(letterGrades)):
            if(letterGrades[i] == letterGradeSearch):
                foundStudents.append(i)
        if(len(foundStudents) > 0):
            print(f"\nStudents with Letter Grade {letterGradeSearch}:")
            for index in foundStudents:
                print(f"{firstNames[index]} {lastNames[index]}, Test1: {test1Scores[index]}, Test2: {test2Scores[index]}, Test3: {test3Scores[index]}, Avg Score: {avgScores[index]:.2f}, Letter Grade: {letterGrades[index]}")
        else:
            print("\nNo students found with the letter grade: ", letterGradeSearch)

    #exit option
    elif(searchOption == "4"):
        print("\nExiting search menu.")
        answer = "n"
    else:
        print("\nInvalid option. Please try again.")

    #repeat search prompt
    if (answer != "n"):
        answer = input("\nWould you like to perform another search? (y/n): ").lower()

#exit message
print("\n\n\tThank you for using the program. Goodbye.\n\n")