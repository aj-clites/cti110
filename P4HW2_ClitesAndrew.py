# Andrew Clites
# 2024-04-09
# P4HW2
# A program that takes an employees name, pay rate, and hours worked and outputs the resulting grows pay and any overtime worked.
# Then allows the user to input as many employees as they want and outputs number of employees entered, total overtime pay,
# total regular pay, and total gross pay.

# Declare Float employeesEntered = 0, totalOvertimePay = 0, totalPay = 0, totalGrossPay = 0
# Declare Float overtimePayList[]
# Declare Float regPayList[]
# Declare Float grossPayList[]
employeesEntered = 0
totalOvertimePay = float(0)
totalPay = float(0)
totalGrossPay = float(0)
overtimePayList = []
regPayList = []
grossPayList = []

# Declare String employee
# Set employee = Input
employee = input("Enter employee's name or 'Done' to terminate: ")
# Declare Float hoursWorked, payRate
# Declare Float overFourty, overTime, time_and_half, overTimePay
# While employee != 'Done'
# 	Set hoursWorked = Input
# 	Set payRate = Input
while employee != 'Done':
	hoursWorked = float(input(f"How many hours did {employee} work? "))
	payRate = float(input(f"What is {employee}'s pay rate? "))
# 	If hoursWorked <= 40 Then
#		Set regHours = hoursWorked
#		Set overFourty = 0
# 	Else
#		Set overFourty = hoursWorked - 40
#		Set regHours = hoursWorked - overFourty
# 	End If
# 	If overFourty > 0 Then
#		Set overTime = overFourty
#		Set time_and_half = payRate * 1.5
# 		Set overTimePay = overTime * time_and_half
#	Else
#		Set overTime = 0
#		Set time_and_half = 0
#		Set overTimePay = 0
# 	End If
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

# 	Declare Float regHoursPay, grossPay
# 	Set regHoursPay = payRate * regHours
# 	Set grossPay = regHoursPay + overTimePay
	regHoursPay = payRate * regHours
	grossPay = regHoursPay + overTimePay

# 	Display "-------------------------------------"
# 	Display "Employee name:"," ", employee
# 	Display "\n"
# 	Display "Hours Worked","  ","Pay Rate","  ","Over Time","  ","OverTime Pay","     ","RegHour Pay","       ","Gross Pay"
# 	Display "---------------------------------------------------------------------------------------------------"
# 	Display "hoursWorked         payRate         overTime         overTimePay            regHoursPay             grossPay"
	print("\n")
	print("Employee name:"," ", employee)
	print("\n")
	print("Hours Worked","  ","Pay Rate","  ","Over Time","  ","OverTime Pay","     ","RegHour Pay","       ","Gross Pay")
	print("---------------------------------------------------------------------------------------------------")
	print(f"{hoursWorked:.1f}            {payRate:.2f}        {overTime:.1f}          ${overTimePay:.2f}            ${regHoursPay:.2f}              ${grossPay:.2f}")
#	Set employeesEntered = employeesEntered + 1
#	Add overTimePay to overtimePayList
#	Add regHoursPay to regPayList
#	Add grossPay to grossPayList
#	Set hoursworked = 0
#	Set regHours = 0
#	Set payRate = 0
#	Set overFourty = 0
#	Set overTime = 0
#	Set overTimePay = 0
#	Set time_and_half = 0
#	Set regHoursPay = 0
#	Set grossPay = 0
	employeesEntered = employeesEntered + 1
	overtimePayList.append(overTimePay)
	regPayList.append(regHoursPay)
	grossPayList.append(grossPay)
	hoursWorked = float(0)
	regHours = float(0)
	payRate = float(0)
	overFourty = float(0)
	overTime = float(0)
	overTimePay = float(0)
	time_and_half = float(0)
	regHoursPay = float(0)
	grossPay = float(0)

#	Set employee = Input
#	Input employee
	employee = input("Enter employee's name or 'Done' to terminate: ")
# End While

# Set totalOverTimePay = sum(overtimePayList)
# Set totalPay = sum(regPayList)
# Set totalGrossPay = sum(grossPayList)
totalOvertimePay = sum(overtimePayList)
totalPay = sum(regPayList)
totalGrossPay = sum(grossPayList)

# Display "Total number of employees entered:", employeesEntered
# Display "Total amount paid for overtime: $", totalOvertimePay
# Display "Total amount paid for regular hours: $", totalPay
# Display "Total amount paid in gross: $", totalGrossPay
print("Total number of employees entered:", employeesEntered)
print(f"Total amount paid for overtime: ${totalOvertimePay:.2f}")
print(f"Total amount paid for regular hours: ${totalPay:.2f}")
print(f"Total amount paid in gross: ${totalGrossPay:.2f}")
	
