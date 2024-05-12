# Andrew Clites
# P5LAB
# 2024-04-18
# A program that takes a year as user input and outputs if has 28 or 29 days in February.

# Define function days_in_feb(user_year)
def days_in_feb(user_year):
    """Run an if-else if-else statement to determine if a year is a leap year or not and assign a variable called days with 28 or 29."""
    if (user_year % 4 == 0) and (user_year % 100 != 0):
        days = 29
    elif user_year % 400 == 0:
        days = 29
    else:
        days = 28
    return days

if __name__ == '__main__':
    # Declare Integer user_input
    # Set user_input = Input
    # Input user_input
    user_input = int(input())

    # Declare days_print = days_in_feb(user_input)
    days_print = days_in_feb(user_input)
    
    # Display user_input, "has", days_print, "days in February."
    print(f"{user_input} has {days_print} days in February.")