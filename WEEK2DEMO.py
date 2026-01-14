

import csv 

total_records = 0 

with open("C:/Users/arman/Documents/GitHub/SE126-ASENDAG-202520/simple.csv") as csvfile:
    file = csv.reader(csvfile) 

    for record in file:
        total_records += 1
        print(record)
        print(record[0], record[1], record[2])

    print("Total Records:", total_records)

