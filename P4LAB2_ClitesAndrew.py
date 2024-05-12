# Andrew Clites
# P4LAB2
# 2024-04-01
# A program that takes two integers as input and outputs the range in increments of 5.

firstInt = int(input())
secondInt = int(input())

if secondInt > firstInt:
    for i in range(firstInt,secondInt+1, 5):
        print(i, end = " ")
    print()
elif secondInt == firstInt:
    print(secondInt, end=" \n")
else:
    print("Second integer can't be less than the first.")