# CTI-110
# P2HW2 - List
# Enki Sell
# October 16 2022
#
# PROMPT for mod1
# GET mod1
# STORE mod1 in module_grades
# PROMPT for mod2
# GET mod2
# STORE mod2 in module_grades
# PROMPT for mod3
# GET mod3
# STORE mod3 in module_grades
# PROMPT for mod4
# GET mod4
# STORE mod4 in module_grades
# PROMPT for mod5
# GET mod5
# STORE mod5 in module_grades
# PROMPT for mod6
# GET mod6
# STORE mod6 in module_grades
# DISPLAY minimum in module_grades
# DISPLAY maximum in module_grades
# DISPLAY sum of module_grades
# DISPLAY average of module_grades
#
#

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

module_avg = float(sum(module_grades)/len(module_grades))
module_avg = round(module_avg, 2)

print("------------Results------------")
print("Lowest Grade:".ljust(20), end="")
print(min(module_grades))
print("Highest Grade:".ljust(20), end="")
print(max(module_grades))
print("Sum of Grades:".ljust(20), end="")
print(sum(module_grades))
print("Average:".ljust(20), end="")
print(module_avg)
print("-------------------------------")
