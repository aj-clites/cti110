# Andrew Clites
# 2024-03-07
# P2HW2_ClitesAndrew
# A program that takes test grades from user input and outputs a list

# Declare Float module1, module2, module3, module4, module5, module6
# Display "Enter grade for Module 1: "
# Input module1
# Display "Enter grade for Module 2: "
# Input module2
# Display "Enter grade for Module 3: "
# Input module3
# Display "Enter grade for Module 4: "
# Input module4
# Display "Enter grade for Module 5: "
# Input module5
# Display "Enter grade for Module 6: "
# Input module6
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Set test_grades = [module1, module2, module3, module4, module5, module6]
test_grades = [module1, module2, module3, module4, module5, module6]

# Set lowestGrade = min(test_grades)
# Set highestGrade = max(test_grades)
# Set sumGrades = sum(test_grades)
# Set averageGrade = sum(test_grades) / 6
lowestGrade = min(test_grades)
highestGrade = max(test_grades)
sumGrades = sum(test_grades)
averageGrade = sum(test_grades) / 6

# Display "------------Results------------"
# Display "Lowest Grade:",   lowestGrade
# Display "Highest Grade:",  highestGrade
# Display "Sum of Grades:",  sumGrades
# Display "Average:",        averageGrade
# Display "---------------------------------------'
print("------------Results------------")
print("Lowest Grade:","     ",f"{lowestGrade:,.1f}")
print("Highest Grade:","    ",f"{highestGrade:,.1f}")
print("Sum of Grades:","    ",f"{sumGrades:,.1f}")
print("Average:","          ",f"{averageGrade:,.2f}")
print("---------------------------------------")


