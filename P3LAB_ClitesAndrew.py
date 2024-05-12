# Andrew Clites
# P3LAB
# 2024-03-13
# A program that takes a year as an integer input and outputs if it is a leap year or not.

# Declare Boolean is_leap_year, leap_year
# Declare Int input_year
# Set input_year = Input
# Set is_leap_year = False
# Set leap_year = input_year MOD 4 == 0 and (input_year MOD 400 == 0 or input_year MOD 100 != 0)
input_year = int(input("Enter a year: "))
is_leap_year = False
leap_year = input_year % 4 == 0 and (input_year % 400 == 0 or input_year % 100 != 0)

# If leap_year == True Then
#   is_leap_year = True
# Else
#   is_leap_year = False
# End If
if leap_year == True:
    is_leap_year = True
else:
    is_leap_year = False

# If is_leap_year == True Then
#   Display input_year, "- leap year"
# Else
#   Display input_year, "- not a leap year"
# End If
if is_leap_year == True:
    print(input_year, "- leap year")
else:
    print(input_year, "- not a leap year")