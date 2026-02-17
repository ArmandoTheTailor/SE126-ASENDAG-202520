#initializing  variables
temp_count = 0
temp_total = 0

answer = "y"


while answer == "y" or answer == "Y":

    tempF = float(input("\t\tEnter temperature in Fahrenheit: "))

    tempC = (tempF - 32) * (5 / 9)

    #math processes
    temp_count += 1     #temp_count = temp_count + 1
    temp_total += tempF #temp_total = temp_total + tempF

    #display data to user
    print(f"\n\t\tTEMP# {temp_count}\tTEMP {tempF:.1f}F = TEMP {tempC:.1f}C\n")

    #loop control
    answer = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        print("***INVALID ENTRY - 'y' or 'n' only!")
        answer = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()

    if answer == "y":
        print("\tAwesome, let's do it!")
    else:
        print("\tOkay, let's take a look at your results!")



#out of loop

#average calculation and conversion
avg_tempF = temp_total / temp_count 

avg_tempC = (avg_tempF - 32) * (5 / 9)


#final displays
print("\n\t\tHere is your final session information: ")
print("\t\tTOTAL TEMPS ENTERED: {0}".format(temp_count))
print("\t\tAVGERAGE TEMP {0:.1f}F  |  {1:.1f}C".format(avg_tempF, avg_tempC))

print("\n\n\t\tThank you for using the program. Goodbye.\n\n")