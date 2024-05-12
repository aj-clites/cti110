# Andrew Clites
# 2024-02-29
# P2LAB1_ClitesAndrew
# A program that takes a input for miles/gallon and dollars/gallon and produces
# the cost of gas for a given distance in miles.


# Declare Float miles_gallon, dollars_gallon
# Set miles_gallon = Input
# Set dollars_gallon = Input
# Display "What is the miles/gallon?"
# Input miles_gallon
# Display "What is the dollars/gallon?
# Input dollars_gallon
miles_gallon = float(input('What is the miles/gallon?\n'))
dollars_gallon = float(input('What is the dollars/gallon?\n'))

# Declare Float gas_cost1, gas_cost2, gas_cost3
# Set gas_cost1 = (20.0 / miles_gallon) * dollars_gallon
# Set gas_cost2 = (75.0 / miles_gallon) * dollars_gallon
# Set gas_cost3 = (500.0 / miles_gallon) * dollars_gallon
gas_cost1 = (20.0 / miles_gallon) * dollars_gallon
gas_cost2 = (75.0 / miles_gallon) * dollars_gallon
gas_cost3 = (500.0 / miles_gallon) * dollars_gallon

# Display f'{gas_cost1:.2f} {gas_cost2:.2f} {gas_cost3:.2f}'
print(f'{gas_cost1:.2f} {gas_cost2:.2f} {gas_cost3:.2f}')
