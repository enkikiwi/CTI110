# Generate random numbers and use them and loops to create a simple math quiz
# November 25 2022
# CTI-110 P5HW2 - Math Quiz
# Enki Sell
#
# generate math quiz based on user input (addition, subtraction)
# use random numbers in quiz, loop while answer is too high or too low
# when answer is correct, return to menu
#

import random

def math_addition(user_option):
    guesses = 0

    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)

    print("  ", num1)
    print("+ ", num2)

    solution = num1 + num2

    user_solution = int(input(""))

    if user_solution == solution:
        guesses += 1
        print("Congratulations! You answered correctly after", guesses, "guesses!")
    else:
        while user_solution > solution:
            guesses += 1
            print("Your guess is too high, please try again.")
            user_solution = int(input(""))
            if user_solution == solution:
                guesses += 1
                print("Congratulations! You answered correctly after", guesses, "guesses!")
            else:
                while user_solution < solution:
                    guesses += 1
                    print("Your guess is too low, please try again.")
                    user_solution = int(input(""))
                    if user_solution == solution:
                        guesses += 1
                        print("Congratulations! You answered correctly after", guesses, "guesses!")
        while user_solution < solution:
            guesses += 1
            print("Your guess is too low, please try again.")
            user_solution = int(input(""))
            if user_solution == solution:
                guesses += 1
                print("Congratulations! You answered correctly after", guesses, "guesses!")
            else:
                while user_solution > solution:
                    guesses += 1
                    print("Your guess is too high, please try again.")
                    user_solution = int(input(""))
                    if user_solution == solution:
                        guesses += 1
                        print("Congratulations! You answered correctly after", guesses, "guesses!")
    return user_option

def math_subtraction(user_option):
    guesses = 0

    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)

    if num1 >= num2:

        print("  ", num1)
        print("- ", num2)

        solution = num1 - num2

        user_solution = int(input(""))

    else:
        print("  ", num2)
        print("- ", num1)

        solution = num2 - num1

        user_solution = int(input(""))

    if user_solution == solution:
        guesses += 1
        print("Congratulations! You answered correctly after", guesses, "guesses!")
    else:
        while user_solution > solution:
            guesses += 1
            print("Your guess is too high, please try again.")
            user_solution = int(input(""))
            if user_solution == solution:
                guesses += 1
                print("Congratulations! You answered correctly after", guesses, "guesses!")
            else:
                while user_solution < solution:
                    guesses += 1
                    print("Your guess is too low, please try again.")
                    user_solution = int(input(""))
                    if user_solution == solution:
                        guesses += 1
                        print("Congratulations! You answered correctly after", guesses, "guesses!")
        while user_solution < solution:
            guesses += 1
            print("Your guess is too low, please try again.")
            user_solution = int(input(""))
            if user_solution == solution:
                guesses += 1
                print("Congratulations! You answered correctly after", guesses, "guesses!")
            else:
                while user_solution > solution:
                    guesses += 1
                    print("Your guess is too high, please try again.")
                    user_solution = int(input(""))
                    if user_solution == solution:
                        guesses += 1
                        print("Congratulations! You answered correctly after", guesses, "guesses!")
    return user_option

print("MAIN MENU")
print("--------------------")
print("1. Adding Random Numbers")
print("2. Subtracting Random Numbers")
print("3. Exit")

user_option = int(input("Please choose one of the menu options:"))

while user_option == 1:
    math_addition(user_option)
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

    user_option = int(input("Please choose one of the menu options:"))
while user_option == 2:
    math_subtraction(user_option)
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

    user_option = int(input("Please choose one of the menu options:"))
if user_option == 3:
    print("Thank you for playing!! Bye!!")
