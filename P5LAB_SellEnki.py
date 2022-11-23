
def days_in_feb(user_year):
        century_years = list(range(100, 2000, 100))
        if user_year in century_years:
                if user_year % 400 == 0:
                        print(user_year, "has 29 days in February.")
                elif not(user_year % 400 == 0):
                        print(user_year, "has 28 days in February.")
        elif user_year % 4 == 0:
                print(user_year, "has 29 days in February.")
        elif not(user_year % 4 == 0):
                print(user_year,  "has 28 days in February.")
   
   
        return user_year

user_year = int(input())
while user_year:
    days_in_feb(user_year)
    user_year = int(input())