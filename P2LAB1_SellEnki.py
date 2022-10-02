miles_gallon = float(input())
dollars_gallon = float(input())

cost_miles = miles_gallon * dollars_gallon

value_1 = dollars_gallon * 20 / miles_gallon
value_2 = dollars_gallon * 75 / miles_gallon
value_3 = dollars_gallon * 500 / miles_gallon

print(f'{value_1:.2f} {value_2:.2f} {value_3:.2f}')