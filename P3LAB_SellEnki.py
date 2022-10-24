is_leap_year = False
century_years = list(range(100, 2000, 100))
   
input_year = int(input())

if input_year in century_years:
    if input_year % 400 == 0:
	    print(input_year, "- leap year")
    elif not(input_year % 400 == 0):
	    print(input_year, "- not a leap year")
elif input_year % 4 == 0:
    print(input_year, "- leap year")
elif not(input_year % 4 == 0):
    print(input_year, "- not a leap year")