#Arman Sendag
#Lab 6
#3-3-2026 (my birthday! huzzah!)

#PROGRAM DESCRIPTION:
'''
Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a small
airplane with seat numbering as follows.
Row
1 A B C D
2 A B C D
3 A B C D
4 A B C D
5 A B C D
6 A B C D
7 A B C D
The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example,
after seats 1A, 2B and 4C are taken the display should look like this:
Row
1 X B C D
2 A X C D
3 A B C D
4 A B X D
5 A B C D
6 A B C D
7 A B C D
After displaying the seats available, the program prompts for the seat desired, the user types in a seat
and then the display of available seats is updated. This continues until all seats are filled or until the user
signals that the program should end. If a user types in a seat that is already assigned, the program
should say that the seat is occupied and ask for another choice.
• You must use a function to display the seating map
• You must use a function that asks the user in they want to continue reserving seats or stop. The
function should only accept an uppercase or lowercase ‘y’ or ‘n’
'''


#VARIABLE DICTIONARY
# seatA: list of seats in column A
# seatB: list of seats in column B
# seatC: list of seats in column C
# seatD: list of seats in column D
# row: variable used to store the row number the user wants to reserve
# seat: variable used to store the seat letter the user wants to reserve
# cont: variable used to control the loop for reserving seats

#--------FUNCTIONS--------------------------------------------
#function to display the seating chart
def displayChart():
    print("Row  Seats")
    print("-"*12)
    for i in range(7):
        print(f"{i+1:<3} {seatA[i]} {seatB[i]:<2} {seatC[i]} {seatD[i]}")

#function to ask user if they want to continue reserving seats
def askContinue():
    cont = "y"
    while cont == "y":
        cont = input("\n\n\tWould you like to reserve another seat? (y/n): ").lower()
        if cont != "y" and cont != "n":
            print("\n\n\tSorry, that is not a valid input. Please try again.")
        else:
            return cont

#--------MAIN EXECUTING CODE--------------------------------

#welcome message
print("\n\n\tWelcome to my Lab 6!")


#7 rows 1-7
#4 seat types A-D

seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]

cont = "y"

#printing the seating chart
print("Here is the seating chart for the airplane:\n")
displayChart()


while cont == "y":
    #ask user for the row 1-7

    row = int(input("\n\n\tPlease enter the row number (1-7): "))
    seat = input("\tPlease enter the seat letter (A-D): ")

    #check seat and replace with X to reserve, or tell user if unavailable
    if seat.upper() == "A":
        if seatA[row-1] == "X":
            print("\n\n\tSorry, that seat is already taken.")
        else:
            seatA[row-1] = "X"

    elif seat.upper() == "B":
        if seatB[row-1] == "X":
            print("\n\n\tSorry, that seat is already taken.")
        else:
            seatB[row-1] = "X"

    elif seat.upper() == "C":
        if seatC[row-1] == "X":
            print("\n\n\tSorry, that seat is already taken.")
        else:
            seatC[row-1] = "X"

    elif seat.upper() == "D":
        if seatD[row-1] == "X":
            print("\n\n\tSorry, that seat is already taken.")
        else:
            seatD[row-1] = "X"
    else:
        print("\n\n\tSorry, that seat is not available. Please try again.")

    #printing the seating chart
    print("Here is the updated seating chart for the airplane:\n")
    displayChart() 
    #ask user if they want to continue
    cont = askContinue()



    print("\n\n\tThank you for using my Lab 6! Have a great day!")