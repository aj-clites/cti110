# Andrew Clites
# 2024-03-19
# P3HW2 Salary
# A program that takes an employees name, pay rate, and hours worked and outputs the resulting grows pay and any overtime worked.

# Declare String employee
# Declare Float hoursWorked, payRate
# Set employee = Input
# Set hoursWorked = Input
# Set payRate = Input
employee = input("Enter employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

# Declare Float overFourty, overTime, time_and_half, overTimePay
# If hoursWorked <= 40 Then
#	Set regHours = hoursWorked
#	Set overFourty = 0
# Else
#	Set overFourty = hoursWorked - 40
#	Set regHours = hoursWorked -overFourty
# End If
# If overFourty > 0 Then
#	Set overTime = overFourty
#	Set time_and_half = payRate * 1.5
# 	Set overTimePay = overTime * time_and_half
# Else
#	Set overTime = 0
#	Set time_and_half = 0
#	Set overTimePay = 0
# End If
if hoursWorked <= 40:
	regHours = hoursWorked
	overFourty = 0
else:
	overFourty = hoursWorked - 40
	regHours = hoursWorked - overFourty
if overFourty > 0:
	overTime = overFourty
	time_and_half = payRate * 1.5
	overTimePay = overTime * time_and_half
else:
	overTime = 0
	time_and_half = 0
	overTimePay = 0

# Declare Float regHoursPay, grossPay
# Set regHoursPay = payRate * regHours
# Set grossPay = regHoursPay + overTimePay
regHoursPay = payRate * regHours
grossPay = regHoursPay + overTimePay

# Display "-------------------------------------"
# Display "Employee name:"," ", employee
# Display "\n"
# Display "Hours Worked","  ","Pay Rate","  ","Over Time","  ","OverTime Pay","     ","RegHour Pay","       ","Gross Pay"
# Display "---------------------------------------------------------------------------------------------------"
# Display "hoursWorked         payRate         overTime         overTimePay            regHoursPay             grossPay"
print("-------------------------------------")
print("Employee name:"," ", employee)
print("\n")
print("Hours Worked","  ","Pay Rate","  ","Over Time","  ","OverTime Pay","     ","RegHour Pay","       ","Gross Pay")
print("---------------------------------------------------------------------------------------------------")
print(f"{hoursWorked:.1f}            {payRate:.1f}        {overTime:.1f}          ${overTimePay:.2f}            ${regHoursPay:.2f}              ${grossPay:.2f}")
