# Andrew Clites
# 2024-03-07
# P2HW1_AndrewClites

# A program that takes a user's input and outputs their budget results.

# Declare Integer budget
# Display 'Enter budget:'
# Input budget
budget = float(input('Enter budget: '))

# Declare String place
# Display 'Enter trave destination here:'
# Input place
place = input('Enter travel destination here: ')

# Delcare Integer gas, accom, food
# Display 'How much do you think you will spend on gas?'
# Input gas
gas = float(input('How much do you think you will spend on gas? '))

# Display 'Approximately how much will you need for accomodation/hotel?'
# Input accom
accom = float(input('Approximately how much will you need for accomodation/hotel? '))

# Display 'Last, how much will you need for food?'
# Input food
food = float(input('Last, how much will you need for food? '))

# Set expenses = gas + accom + food
expenses = gas + accom + food

# Set result = budget - expenses
result = budget - expenses

# Display '-----------Travel Expenses-----------'
# Display 'Location:', place
# Display 'Initial Budget:', '$',budget

print('------------Travel Expenses------------')
print('Location:','          ',place)
print('Initial Budget:','    ',f'${budget:,.2f}')

# Display 'Fuel:', '$',gas
# Display 'Accomodation:', '$',accom
# Display 'Food:', '$',food
# Display '-------------------------------------'
print('Fuel:','              ',f'${gas:,.2f}')
print('Accomodation:','      ',f'${accom:,.2f}')
print('Food:','              ',f'${food:,.2f}')
print('---------------------------------------')

# Display 'Remaining Balance:', '$',result
print('\n')
print('Remaining Balance:',' ',f'${result:,.2f}')
