# Andrew Clites
# 2024-02-29
# P2LAB2_ClitesAndrew
# A program that takes 4 floating-point inputs and outputs the product and
# average both rounded and to the thousandths place.

# Declare Float num1, num2, num3, num4
# Set num1 = Input
# Set num2 = Input
# Set num3 = Input
# Set num4 = Input
# Display "First number:"
# Input num1
# Display "Second number:"
# Input num2
# Display "Third number:"
# Input num3
# Display "Fourth Number:"
# Input num4
num1 = float(input('First Number:\n'))
num2 = float(input('Second Number:\n'))
num3 = float(input('Third Number:\n'))
num4 = float(input('Fourth Number:\n'))

# Declare Float product, average
# Set product = num1 * num2 * num3 * num4
# Set average = (num1 + num2 + num3 + num4) / 4
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# Display product, average (both rounded)
# Display proudct, average (both to the thousandths place)
print(f'{product:.0f} {average:.0f}')
print(f'{product:.3f} {average:.3f}')
