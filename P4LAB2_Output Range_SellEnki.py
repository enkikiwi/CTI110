user_num1 = int(input())
user_num2 = int(input())

if user_num2 < user_num1:
    print("Second integer can't be less than the first.")

else: 
    while user_num1 <= user_num2:
        print(user_num1, end = ' ')
        user_num1 = user_num1 + 5   
    print()