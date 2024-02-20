# Andrew Clites

# 2024-02-20

# P1HW2_ClitesAndrew

# A program that takes a user's input and outputs their budget results.

# Declare Integer budget
# Display 'Enter budget:'
# Input budget
budget = int(input('Enter budget: '))

# Declare String place
# Display 'Enter trave destination here:'
# Input place
place = input('Enter travel destination here: ')

# Delcare Integer gas, accom, food
# Display 'How much do you think you will spend on gas?'
# Input gas
gas = int(input('How much do you think you will spend on gas? '))

# Display 'Approximately how much will you need for accomodation/hotel?'
# Input accom
accom = int(input('Approximately how much will you need for accomodation/hotel? '))

# Display 'Last, how much will you need for food?'
# Input food
food = int(input('Last, how much will you need for food? '))

# Set expenses = gas + accom + food
expenses = gas + accom + food

# Set result = budget - expenses
result = budget - expenses

# Display '-----------Travel Expenses-----------'
# Display 'Location:', place
# Display 'Initial Budget:', budget

print('------------Travel Expenses------------')
print('Location:', place)
print('Initial Budget:', budget)

# Display 'Fuel:', gas
# Display 'Accomodation:', accom
# Display 'Food:', food
print('\n')
print('Fuel:', gas)
print('Accomodation:', accom)
print('Food:', food)

# Display 'Remaining Balance:', result
print('\n')
print('Remaining Balance:', result)
