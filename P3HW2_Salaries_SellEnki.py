# CTI-110
# P3HW2 - Salary
# Enki Sell
# October 29 2022
#
# Get Employee name, Hours Worked for the week, and pay rate from user
# Determine if overtime has been reached and if so how much the employee gets compensated for it
# Calculate pay for regular hours
# Display Employee name, pay rate, hours worked, overtime hours, overtime pay, regular pay, and gross pay
#

name = input("Enter emplyee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))


from decimal import Decimal


if Decimal(hours)>= Decimal(40):
    overtime = hours-40    
    overtime_pay = overtime*(pay*1.5)
    reg_hour = hours-overtime
else:
    overtime = 0
    overtime_pay = 0
    reg_hour = hours-overtime

reg_pay = reg_hour*pay
gross_pay = reg_pay+overtime_pay

print("-------------------------------------")
print("Employee name:".ljust(20), name)
print("")
print("Hours Worked".ljust(20), "Pay Rate".ljust(20), "OverTime".ljust(20), "OverTime Pay".ljust(20), "RegHour Pay".ljust(20), "Gross Pay".ljust(20))
print("--------------------------------------------------------------------------------------------------------------------------")
print(f'{hours:<20.1f} {pay:<20.1f} {overtime:<20.1f} {overtime_pay:<20.2f} ${reg_pay:<20.2f} ${gross_pay:<20.2f}')
