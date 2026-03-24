#Arman Sendag
#Lab 5
#2-23-2026

#PROGRAM DESCRIPTION:
'''
Build a personal library search system using the file book_list.csv. It is set up as follows:
book_list.csv fields
Field # File Data
0 Library Number (unique)
1 Title
2 Author
3 Genre
4 Page Count
5 Status: Available/On Loan
Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.
Your program should give your user the following menu:
Personal Library Menu
1. Show All Titles – list all book data to the user
a. +10 bonus points if it is displayed alphabetically by title (and all other searches still work)
2. Search by Title – allow for an entire title or a title key word – SEQUENTIAL SEARCH
3. Search by Author – show all titles of the searched-for author – SEQUENTIAL SEARCH
4. Search by Genre - show all titles of the searched-for genre – SEQUENTIAL SEARCH
5. Search by Library Number – only allow for one specific library number item – BINARY SEARCH
6. Show All Available – show all titles with status “available” – SEQUENTIAL SEARCH
7. Show All On Loan - show all titles with status “on loan” – SEQUENTIAL SEARCH
8. EXIT
When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author,
Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches
should not be case sensitive.

'''


#VARIABLE DICTIONARY
# libraryNumbers: list of library numbers
# titles: list of book titles
# authors: list of book authors
# genres: list of book genres
# pageCounts: list of book page counts
# statuses: list of book statuses (Available/On Loan)
# found: list of indices of found search results
# option: variable used to control the search menu loop
# totalRecords: variable used to track the total number of records in the lists
# search: variable used to store the user's search input

#--------FUNCTIONS--------------------------------------------

#display function 
def display(index):
    print(f"{libraryNumbers[index]:15} {titles[index]:25} {authors[index]:20} "
        f"{genres[index]:15} {pageCounts[index]:10} {statuses[index]:<12}")


#--------MAIN EXECUTING CODE--------------------------------

#setting variables
libraryNumbers = []
titles = []
authors = []
genres = []
pageCounts = []
statuses = []
found = []
option = "0"
totalRecords = 0

#importing csv module
import csv

with open('C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/book_list.csv') as csvfile:
    file = csv.reader(csvfile)


    for record in file:
        libraryNumbers.append(record[0])
        titles.append(record[1])
        authors.append(record[2])
        genres.append(record[3])
        pageCounts.append(record[4])
        statuses.append(record[5])

        totalRecords += 1

#search menu
while option != "8":

    print("\n\n\tPersonal Library Menu")
    print("1. Show All Titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Show All Available")  
    print("7. Show All On Loan")
    print("8. EXIT")

    option = input("Please select an option (1-8): ")

    #show all titles
    if option == "1":
        print(f"\n{'LIBRARY #':15} {'TITLE':25} {'AUTHOR':20} "
        f"{'GENRE':15} {'PAGES':10} {'STATUS':12}")
        print("-" * 100)
        for i in range(0, totalRecords):
            display(i)
    #search by title
    elif option == "2":
        search = input("Enter the title or a keyword to search for: ").lower()
        found = []
        for i in range(0, totalRecords):
            if search in titles[i].lower():
                found.append(i)
        if len(found) > 0:
            print(f"\n{'LIBRARY #':15} {'TITLE':25} {'AUTHOR':20} "
            f"{'GENRE':15} {'PAGES':10} {'STATUS':12}")
            print("-" * 100)
            for index in found:
                display(index)
        else:
            print("No titles found matching that search.")
    #search by author
    elif option == "3":
        search = input("Enter the author to search for: ").lower()
        found = []
        for i in range(0, totalRecords):
            if search in authors[i].lower():
                found.append(i)
        if len(found) > 0:
            print(f"\n{'LIBRARY #':15} {'TITLE':25} {'AUTHOR':20} "
            f"{'GENRE':15} {'PAGES':10} {'STATUS':12}")
            print("-" * 100)
            for index in found:
                display(index)
        else:
            print("No titles found matching that search.")
    #search by genre
    elif option == "4":
        search = input("Enter the genre to search for: ").lower()
        found = []
        for i in range(0, totalRecords):
            if search in genres[i].lower():
                found.append(i)
        if len(found) > 0:
            print(f"\n{'LIBRARY #':15} {'TITLE':25} {'AUTHOR':20} "
            f"{'GENRE':15} {'PAGES':10} {'STATUS':12}")
            print("-" * 100)
            for index in found:
                display(index)
        else:
            print("No titles found matching that search.")
    #search by library number
    elif option == "5":
        search = input("Enter the library number to search for: ")
        found = -1
        for i in range(0, totalRecords):
            if search == libraryNumbers[i]:
                found = i
        if found != -1:
            print(f"\n{'LIBRARY #':15} {'TITLE':25} {'AUTHOR':20} "
            f"{'GENRE':15} {'PAGES':10} {'STATUS':12}")
            print("-" * 100)
            display(found)
        else:
            print("No titles found matching that search.")
    #show all available
    elif option == "6":
        found = []
        for i in range(0, totalRecords):
            if statuses[i].lower() == "available":
                found.append(i)
        if len(found) > 0:
            print(f"\n{'LIBRARY #':15} {'TITLE':25} {'AUTHOR':20} "
            f"{'GENRE':15} {'PAGES':10} {'STATUS':12}")
            print("-" * 100)
            for index in found:
                display(index)
        else:
            print("No titles found matching that search.")
    #show all on loan
    elif option == "7":
        found = []
        for i in range(0, totalRecords):
            if statuses[i].lower() == "on loan":
                found.append(i)
        if len(found) > 0:
            print(f"\n{'LIBRARY #':15} {'TITLE':25} {'AUTHOR':20} "
            f"{'GENRE':15} {'PAGES':10} {'STATUS':12}")
            print("-" * 100)
            for index in found:
                display(index)
        else:
            print("No titles found matching that search.")

print("\n\n\tThank you for using the Personal Library Search System. Goodbye!")