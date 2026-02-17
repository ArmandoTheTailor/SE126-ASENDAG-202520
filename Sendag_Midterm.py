#Arman Sendag
#Midterm Exam
#2-9-2026

#PROGRAM DESCRIPTION:
'''
Choice 3

Read data from student file and store to 1D parallel lists. Create a new list to hold student IDs for each student. Each student should have a unique ID and the first should be 10001, each students ID should be unique and the ID values should not exceed 10021. Once the new list is populated, reprint the data to the console including the student ID for each student. Display all student data to a user in a formatted table.

'''


#VARIABLE DICTIONARY
# firstNames: list of students' first names
# lastNames: list of students' last names
# departments: list of students' departments
# gpas: list of students' GPAs
# studentIDs: list of students' unique IDs
# file: variable used to read from and write to files
# answer: variable used to control the search menu loop
# searchOption: variable used to store the user's choice of search type
# lastNameSearch: variable used to store the last name input for searching
# departmentSearch: variable used to store the department input for searching
# found: variable used to track if a search result is found and its index in the lists

#--------FUNCTIONS--------------------------------------------


#--------MAIN EXECUTING CODE--------------------------------

#importing csv module
import csv

#welcome message
print("\n\n\tWelcome to my Midterm Lab!")

#initializing lists
firstNames = []
lastNames = []
departments = []
gpas = []
studentIDs = []




#connecting to file
with open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/students.csv") as csvfile:
    file = csv.reader(csvfile) 
    for record in file:
        #appends each field to respective list
        firstNames.append(record[0])
        lastNames.append(record[1])
        departments.append(record[2])
        gpas.append(float(record[3]))
#disconnects from file



#creates a header for the output
print ("\n\n\tStudent Records:\n")
print(f"{'First Name':<15}{'Last Name':<15}{'Department':<15}{'GPA':<10}{'Student ID':<12}")
print("-" * 87)
#prints each student's full information
for i in range(len(firstNames)):
    studentID = 10001 + i
    studentIDs.append(studentID)
    print(f"{firstNames[i]:<15}{lastNames[i]:<15}{departments[i]:<15}{gpas[i]:<10.2f}{studentIDs[i]:<12}")
print("-" * 87)
print("\n\n\tTotal Students:", len(firstNames))  

#write data to new csv file
file = open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/midterm_choice3.csv", "w")
for i in range (len(firstNames)):
    file.write(f"{firstNames[i]},{lastNames[i]},{departments[i]},{gpas[i]},{studentIDs[i]}\n")
file.close()

#sequential search menu
print("\n\n\tWelcome to Student Search Menu")
answer = input("\nWould you like to search for a student? (y/n): ").lower()
while(answer == "y"):
    print("\n\n\tSearch Menu:")
    print("\n1. Search by LAST name")
    print("2. Search by Department")
    print("3. Exit")

    searchOption = input("\nPlease enter the number of your search option: ")

    #last name search
    if(searchOption == "1"):
        lastNameSearch = input("\nEnter the LAST name of the student you are searching for: ")
        found = -1
        for i in range(len(lastNames)):
            if(lastNames[i].lower() == lastNameSearch.lower()):
                found = i
        if(found != -1):
            print(f"\nStudent Found:\n{firstNames[found]} {lastNames[found]}, Department: {departments[found]}, GPA: {gpas[found]:.2f}, Student ID: {studentIDs[found]}")
        else:
            print("\nNo student found with the last name: ", lastNameSearch)
    
    #department search which lists all students in the department
    elif(searchOption == "2"):
        departmentSearch = input("\nEnter the Department you are searching for: ")
        found = False
        print(f"\nStudents in {departmentSearch} Department:")
        for i in range(len(departments)):
            if(departments[i].lower() == departmentSearch.lower()):
                found = True
                print(f"{firstNames[i]} {lastNames[i]}, Department: {departments[i]}, GPA: {gpas[i]:.2f}, Student ID: {studentIDs[i]}")
        if(not found):
            print("\nNo students found in the department: ", departmentSearch)

    #exit option
    elif(searchOption == "3"):
        print("\nExiting search menu.")
        answer = "n"
    else:
        print("\nInvalid option. Please try again.")

    #repeat search prompt
    if (answer != "n"):
        answer = input("\nWould you like to perform another search? (y/n): ").lower()

#exit message
print("\n\n\tThank you for using the program. Goodbye.\n\n")