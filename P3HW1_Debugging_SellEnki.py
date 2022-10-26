# CTI-110
# P2HW2 - List
# Enki Sell
# October 26 2022
#
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

from decimal import Decimal

grades_low = min(grades)
grades_high = max(grades)
grades_sum = sum(grades)
grades_avg = Decimal((sum(grades))/len(grades))
grades_avg = Decimal(round(grades_avg, 2))

# determine letter grade for average

print("------------Results------------")
print("Lowest Grade:".ljust(20), end="")
print(grades_low)
print("Highest Grade:".ljust(20), end="")
print(grades_high)
print("Sum of Grades:".ljust(20), end="")
print(grades_sum)
print("Average:".ljust(20), end="")
print(grades_avg)
print("-------------------------------")


if Decimal(grades_avg) >= Decimal(90):
    print('Your grade is: A')
elif Decimal(grades_avg) >= Decimal(80):
    print('Your grade is: B')
elif Decimal(grades_avg) >= Decimal(70):
    print('Your grade is: C')
elif Decimal(grades_avg) >= Decimal(60):
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this





