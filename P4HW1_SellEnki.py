# CTI-110
# P4HW1 - Score List
# Enki Sell
# November 12 2022
#
# Ask user for number of input scores
# Use user input in a loop to collect scores
# Check if score entered is valid; if not ask for score again
# Add scores to list
# Show lowest score, then drop it from the list
# Show list after dropping the lowest score
# Show average of modified list
# Determine and display letter grade for calculated average
#

from decimal import Decimal

score_number = int(input("How many scores do you want to enter?"))
increment = 1
module_grades = []

for i in range(score_number):
    print("Enter score #", increment, ":", end = " ")
    score = float(input())

    if 100 < score:
        while score > 100:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print("Enter score #", increment, "again:", end = " ")
            score = float(input())
        while score < 0:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print("Enter score #", increment, "again:", end = " ")
            score = float(input())
        increment = increment + 1
        module_grades.append(score)
    elif score < 0:
        while score < 0:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print("Enter score #", increment, "again:", end = " ")
            score = float(input())
        while score > 100:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print("Enter score #", increment, "again:", end = " ")
            score = float(input())
        increment = increment + 1
        module_grades.append(score)
    
    else:
        increment = increment + 1
        module_grades.append(score)
    

print("------------Results------------")
print("Lowest Grade:".ljust(20), end="")
print(min(module_grades))

module_grades.remove(min(module_grades))

print("Modified List:".ljust(20), end="")
print(module_grades)

module_avg = sum(module_grades) / len(module_grades)

print("Scores Average:".ljust(20), end="")
print(module_avg)

if Decimal(module_avg) >= Decimal(90):
    letter_grade = "A"
elif Decimal(module_avg) >= Decimal(80):
    letter_grade = "B"
elif Decimal(module_avg) >= Decimal(70):
    letter_grade = "C"
elif Decimal(module_avg) >= Decimal(60):
    letter_grade = "D"
else:
    letter_grade = "F"

print("Grade:".ljust(20), end="")
print(letter_grade)

print("-------------------------------")
