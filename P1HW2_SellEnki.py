
 # Travel Expense Interactive Python File
 
 # September 24 2022
 
 # CTI-110 P1HW2 - Travel Expense
 
 # Enki Sell
 
 #
 
print('This program calculates and displays travel expenses')
budg = int(input('Enter budget:\n'))
dest = input('Enter your travel destination:\n')
gas = int(input('How much do you think you will spend on gas? \n'))
hotel = int(input('Approximately, how much will you need for accomodation/hotel? \n'))
food = int(input('Last, how much do you need for food?\n'))
expenses = gas + hotel + food
 
print('------------Travel Expenses------------')
print('Location:', dest)
print('Initial Budget:', budg)
print()
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print()
print('Remaining Balance:', budg-expenses)
