
 # Travel Expense Interactive Python File, Refined Output Display
 
 # October 8 2022
 
 # CTI-110 P2HW1 - Travel Expense
 
 # Enki Sell
 
 #
 
print('This program calculates and displays travel expenses')

# budg is the variable in which the user's full budget will be stored
budg = int(input('Enter budget:\n'))
# dest is the variable in which the user's destination string will be stored
dest = input('Enter your travel destination:\n')
# gas is the variable in which the amount of money the user spends on gas will be stored
gas = int(input('How much do you think you will spend on gas? \n'))
# hotel is the variable in which the amount of money the user spends on accomodation will be stored
hotel = int(input('Approximately, how much will you need for accomodation/hotel? \n'))
# food is the variable in which the amount of money the user spends on food will be stored
food = int(input('Last, how much do you need for food?\n'))
# expenses is the variable in which the total amount of money the user has spent will be stored, in order to be used in mathematical functions with the budget variable
expenses = gas + hotel + food
 
print('------------Travel Expenses------------')

#prints the user defined destination with the Location tag
print(('Location:').ljust(20), end='')
print(dest)

#prints the user defined budget with the Initial Budget tag
print('Initial Budget:'.ljust(20), end='')
print('$'+f'{budg:.1f}')

#prints the user defined gas cost with the Fuel tag
print('Fuel:'.ljust(20), end='')
print('$'+f'{gas:.1f}')

#prints the user defined hotel cost with the Accomodation tag
print('Accomodation:'.ljust(20), end='')
print('$'+f'{hotel:.1f}')

#prints the user defined food cost with the Food tag
print('Food:'.ljust(20), end='')
print('$'+f'{food:.1f}')

print('---------------------------------------')

#takes the total expenses as derived from the addition of the user define gas, hotel, and food, then subtracts that from the user defined budget, then prints the answer with the Remaining Balance tag
print('Remaining Balance:'.ljust(20), end='')
print('$'+f'{budg - expenses:.1f}')
