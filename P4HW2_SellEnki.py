# CTI-110
# P4HW2 - Salary Calculator
# Enki Sell
# November 15 2022
#
# Use a loop
# Get Employee name, Hours Worked for the week, and pay rate from user
# Determine if overtime has been reached and if so how much the employee gets compensated for it
# Calculate pay for regular hours
# Exit the loop
# Display Employee name, pay rate, hours worked, overtime hours, overtime pay, regular pay, and gross pay
# Include multiple employees

from decimal import Decimal

increment = 0
overtime_total = 0
reg_hours_total = 0
gross_total = 0
reg_pay = []
overtime_pay = []
gross_pay = []
name = input("Enter emplyee's name or 'None' to terminate: ")

while name != 'None':
    increment = increment + 1
    print("How many hours did", name, "work?", end= " ")
    hours = float(input())
    print("What is", name, "'s pay rate?", end= " ")
    pay = float(input())

    if Decimal(hours)>= Decimal(40):
        overtime = hours - 40
        emp_overtime_pay = overtime * (pay * 1.5)
        overtime_pay.append(emp_overtime_pay)
        reg_hour = hours - overtime
        emp_reg_pay = reg_hour * pay
        emp_gross_pay = emp_overtime_pay + emp_reg_pay
    else:
        overtime = 0
        overtime_pay.append(0)
        emp_overtime_pay = 0
        reg_hour = hours - overtime
        emp_reg_pay = reg_hour * pay
        emp_gross_pay = hours * pay
        emp_gross_pay = emp_overtime_pay + emp_reg_pay

    reg_pay.append(reg_hour * pay)
    gross_pay.append(emp_gross_pay)

    print("-------------------------------------")
    print("Employee name:".ljust(20), name)
    print("")
    print("Hours Worked".ljust(20), "Pay Rate".ljust(20), "OverTime".ljust(20), "OverTime Pay".ljust(20), "RegHour Pay".ljust(20), "Gross Pay".ljust(20))
    print("--------------------------------------------------------------------------------------------------------------------------")
    print(f'{hours:<20.1f} {pay:<20.1f} {overtime:<20.1f} {emp_overtime_pay:<20.2f} ${emp_reg_pay:<20.2f} ${emp_gross_pay:<20.2f}')
    print('')
    name = input("Enter emplyee's name or 'None' to terminate: ")

print("Total number of employees entered: ", increment)
print("Total amount paid for overtime: $", sum(overtime_pay))
print("Total amount paid for regular hours: $", sum(reg_pay))
print("Total amount paid in gross: $", sum(gross_pay))
