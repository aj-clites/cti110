# Andrew Clites
# 2024-04-09
# P4HW1_ClitesAndrew
# A program that takes test grades from user input and outputs the lowest score, a modified list, average grade, and average letter grade.

# Declare int numScores
# Set numScores = Input
# Display "How many scores do you want to enter? "
# Input numScores
numScores = int(input("How many scores do you want to enter? "))

# Declare Float test_grades[]
test_grades = []

# For i = 1 To numScores+1
#   Display "Enter score #", i, ": "
#   Set gradeInput = Input
#   Add gradeInput to test_grades
#   Input gradeInput
#   While gradeInput < 0 or gradeInput > 100
#       Display "INVALID Score entered!!!"
#       Display "Score should be between 0 and 100"
#       Remove last item from list
#       Display "Enter score #", i, "again: "
#       Set gradeInput = Input
#       Input gradeInput
#       Add new grade input to test_grades
#   End While
#   Set i = i + 1
# End For
for i in range(1, numScores+1):
    gradeInput = float(input(f"Enter score #{i:.0f}: "))
    test_grades.append(gradeInput)
    while gradeInput < 0 or gradeInput > 100:
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")
        test_grades.pop()
        gradeInput = float(input(f"Enter score #{i:.0f} again: "))
        test_grades.append(gradeInput)
        break
    i = i + 1

# Set lowestGrade = min(test_grades)
# Remove lowest value in test_grades
# Declare modifiedList[]
# Set modifiedList = test_grades
# Set averageGrade = sum(modifiedList) / (numScores - 1)
lowestGrade = min(test_grades)
test_grades.remove(min(test_grades))
modifiedList = test_grades
averageGrade = sum(modifiedList) / (numScores - 1)

# Declare Character letterGrade = 'A'
# If averageGrade >= 90 Then
#   Set letterGrade = 'A'
# Else If averageGrade >= 80 Then
#   Set letterGrade = 'B'
# Else If averageGrade >= 70 Then
#   Set letterGrade = 'C'
# Else If averageGrade >= 60 Then
#   Set letterGrade = 'D'
# Else
#   Set letterGrade = 'F'
# End If
letterGrade = 'A'
if averageGrade >= 90:
    letterGrade = 'A'
elif averageGrade >= 80:
    letterGrade = 'B'
elif averageGrade >= 70:
    letterGrade = 'C'
elif averageGrade >= 60:
    letterGrade = 'D'
else:
    letterGrade = 'F'

# Display "------------Results------------"
# Display "Lowest Grade:",  lowestGrade
# Display "Modified List:", modifiedList
# Display "Score Average:", averageGrade
# Display "Grade        :", letterGrade
# Display "---------------------------------------'
print("------------Results------------")
print(f"Lowest Grade:  {lowestGrade:,.1f}")
print(f"Modified List: {modifiedList}")
print(f"Score Average: {averageGrade:,.2f}")
print(f"Grade        : {letterGrade}")
print("---------------------------------------")


