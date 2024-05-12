# Andrew Clites
# P3HW1
# 2024-03-13
# This program takes a number grade , determines average and displays letter grade for average.

# Declare Float mod_1, mod_2, mod_3, mod_4, mod_5, mod_6
# Display "Enter grade for Module 1: "
# Set mod_1 = Input
# Display "Enter grade for Module 2: "
# Set mod_2 = Input
# Display "Enter grade for Module 3: "
# Set mod_3 = Input
# Display "Enter grade for Module 4: "
# Set mod_4 = Input
# Display "Enter grade for Module 5: "
# Set mod_5 = Input
# Display "Enter grade for Module 6: "
# Set mod_6 = Input
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 1: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))


# Declare Float grades
# Set grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Declare Float lowGrade, highGrade, sumGrades, avgGrade
# Set lowGrade = min(grades)
# Set highGrade = max(grades)
# Set sumGrades = sum(grades)
# Set avgGrade = (sum(grades)) / 6
lowGrade = min(grades)
highGrade = max(grades)
sumGrades = sum(grades)
avgGrade = (sum(grades)) / 6

# If avgGrade >= 90 Then
# 	letterGrade = "A"
# Else If avgGrade >= 80 Then
#	letterGrade = "B"
# Else If avgGrade >= 70 Then
#	letterGrade = "C"
# Else If avgGrade >= 60 Then
#	letterGrade = "D"
# Else
#	letterGrade = "F"
# End If
if avgGrade >= 90:
	letterGrade = "A"
elif avgGrade >= 80:
 	letterGrade = "B"
elif avgGrade >= 70:
	letterGrade = "C"
elif avgGrade >= 60:
	letterGrade = "D"
else:
	letterGrade = "F"

# Display "------------Results------------"
# Display "Lowest Grade:","  ", lowGrade
# Display "Highest Grade:"," ", highGrade
# Display "Sum of Grades:"," ", sumGrades
# Display "Average:","       ", avgGrade
# Display "----------------------------------------"
# Display "Your grade is: ", letterGrade 
print("------------Results------------")
print("Lowest Grade:","  ",f"{lowGrade:.1f}")
print("Highest Grade:"," ",f"{highGrade:.1f}")
print("Sum of Grades:"," ",f"{sumGrades:.1f}")
print("Average:","       ",f"{avgGrade:.2f}")
print("----------------------------------------")
print("Your grade is: ",letterGrade)







