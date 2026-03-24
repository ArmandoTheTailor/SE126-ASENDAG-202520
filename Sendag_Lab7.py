#Arman Sendag
#Lab 7
#3-3-2026 (my birthday! huzzah!)

#PROGRAM DESCRIPTION:
'''
Build a mini programming dictionary a user can search through and add to using the words.csv file:
words.csv fields
Field # File Data
0 Word (unique)
1 Definition
Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and
the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a
user to interact with the dictionary based on the following menu:
My Programming Dictionary Menu
1. Show all words – Show all words and their definitions stored to the dictionary
2. Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if
the word is not in the dictionary)
3. Add a word – Allow a user to add a word and its definition to the dictionary if it does not already exist
4. EXIT
The program should not be case sensitive for user input, and the user should only be able to quit when they have
selected menu option number 4.

Bonus #1 [+5]: When the user is finished using the program, create a new file called updated_words.csv which contains
the entire dictionary (including any new words added during the session) and follows the original words.csv field
structure (first field is the word, second field is the definition).
'''


#VARIABLE DICTIONARY
#menuChoice: variable used to control the menu loop
#searchWord: variable used to store the word the user wants to search for
#newWord: variable used to store the word the user wants to add
#newDefinition: variable used to store the definition for the new word
#file: variable used to store the file object for the updated_words.csv file
#dictionary: dictionary object used to store the words and definitions from the words.csv file

#--------FUNCTIONS--------------------------------------------


#--------MAIN EXECUTING CODE--------------------------------

import csv

dictionary = {}

with open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for record in file:
        dictionary.update({record[0]: [record[1]]})

menuChoice = 0

while menuChoice != 4:
    print("\n\n\tMy Programming Dictionary Menu")
    print("1. Show all words")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. EXIT")

    menuChoice = int(input("\n\n\tPlease select an option (1-4): "))

    if menuChoice == 1:
        for key in dictionary:
            print(f"\n\n\t{key}: {dictionary[key][0]}")

    elif menuChoice == 2:
        searchWord = input("\n\n\tPlease enter the word you would like to search for: ").lower()
        if searchWord in dictionary:
            print(f"\n\n\t{searchWord}: {dictionary[searchWord][0]}")
        else:
            print(f"\n\n\tSorry, {searchWord} is not in the dictionary.")

    elif menuChoice == 3:
        newWord = input("\n\n\tPlease enter the word you would like to add: ").lower()
        if newWord in dictionary:
            print(f"\n\n\tSorry, {newWord} is already in the dictionary.")
        else:
            newDefinition = input("\n\n\tPlease enter the definition for the word: ")
            dictionary.update({newWord: [newDefinition]})
            print(f"\n\n\t{newWord} has been added to the dictionary.")
    elif menuChoice == 4:
        print("\n\n\tExiting the program...")
    else:
        print("\n\n\tSorry, that is not a valid option. Please try again.")

#creating a new file called updated_words.csv which contains the entire dictionary (including any new words added during the session) and follows the original words.csv field structure (first field is the word, second field is the definition).
file = open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/updated_words.csv", "w")
for key in dictionary:
    file.write(f"{key},{dictionary[key][0]}\n")
file.close()

print("\n\n\tThank you for using my Programming Dictionary! Have a great day!")