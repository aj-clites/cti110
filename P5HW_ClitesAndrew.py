# Andrew Clites
# 2024-04-27
# P5HW
# A program that lets a user take a math quiz.

import random

# Function Integer addingQuiz()
def addingQuiz():
    # Declare Integer add1, add2
    # Set add1 = random.randint(1, 999)
    # Set add2 = random.randint(1, 999)
    add1 = random.randint(1, 999)
    add2 = random.randint(1, 999)

    # Display ""
    # Display " ", add1
    # Display "+", add2
    # Declare addAnswer, correctAddAnswer, attempts
    # Display "Enter answer: "
    # Set addAnswer = Input
    # Input addAnswer
    # Set correctAddAnswer = add1 + add2
    # Set attempts = 0
    print("")
    print(" ", add1)
    print("+", add2)
    addAnswer = int(input("Enter answer: "))
    correctAddAnswer = add1 + add2
    attempts = 0

    # While addAnswer != correctAddAnswer
    while addAnswer != correctAddAnswer:

    #   If addAnswer > correctAddAnswer Then
    #       Display ""
    #       Display addAnswer, "is to high. Please try again."
    #       Display ""
    #       Display " ", add1
    #       Display "+", add2
    #       Display "Try again: "
    #       Set addAnswer = Input
    #       Input addAnswer
    #       Set attempts += 1
    #   Else If addAnswer < correctAddAnswer Then
    #       Display ""
    #       Display addAnswer, "is to low. Please try again."
    #       Display ""
    #       Display " ", add1
    #       Display "+", add2
    #       Display "Try again: "
    #       Set addAnswer = Input
    #       Input addAnswer
    #       Set attempts += 1
    #   End If
        if addAnswer > correctAddAnswer:
            print("")
            print(addAnswer, "is to high. Please try again.")
            print("")
            print(" ", add1)
            print("+", add2)
            addAnswer = int(input("Try again: "))
            attempts += 1
        elif addAnswer < correctAddAnswer:
            print("")
            print(addAnswer, "is to low. Please try again.")
            print("")
            print(" ", add1)
            print("+", add2)
            addAnswer = int(input("Try again: "))
            attempts += 1
    # If addAnswer == correctAddAnswer Then
    #   Set attempts += 1
    #   Display ""
    #   Display "Attempts: ", attempts
    #   Display ""
    #   Display "Congradulations, ", addAnswer, "is correct."
    # End If
    if addAnswer == correctAddAnswer:
        attempts += 1
        print("")
        print("Attempts: ", attempts)
        print("")
        print("Congradulations, ", addAnswer, "is correct.")
    # End While
# End Function

# Function Integer subtractingQuiz()
def subtractingQuiz():
    # Declare Integer sub1, sub2
    # Set sub1 = random.randint(1, 999)
    # Set sub2 = random.randint(1, 999)
    sub1 = random.randint(1, 999)
    sub2 = random.randint(1, 999)

    # Display ""
    # Display " ", sub1
    # Display "-", sub2
    # Declare subAnswer, correctSubAnswer, attempts
    # Display "Enter answer: "
    # Set subAnswer = Input
    # Input subAnswer
    # Set correctSubAnswer = sub1 + sub2
    # Set attempts = 0
    print("")
    print(" ",sub1)
    print("-", sub2)
    subAnswer = int(input("Enter answer: "))
    correctSubAnswer = sub1 - sub2
    attempts = 0

    # While subAnswer != correctSubAnswer
    while subAnswer != correctSubAnswer:

    #   If subAnswer > correctSubAnswer Then
    #       Display ""
    #       Display subAnswer, "is to high. Please try again."
    #       Display ""
    #       Display " ", sub1
    #       Display "+", sub2
    #       Display "Try again: "
    #       Set subAnswer = Input
    #       Input subAnswer
    #       Set attempts += 1
    #   Else If subAnswer < correctSubAnswer Then
    #       Display ""
    #       Display subAnswer, "is to low. Please try again."
    #       Display ""
    #       Display " ", sub1
    #       Display "+", sub2
    #       Display "Try again: "
    #       Set subAnswer = Input
    #       Input subAnswer
    #       Set attempts += 1
    #   End If
        if subAnswer > correctSubAnswer:
            print("")
            print(subAnswer, "is to high. Please try again.")
            print("")
            print(" ", sub1)
            print("-", sub2)
            subAnswer = int(input("Try again: "))
            attempts += 1
        elif subAnswer < correctSubAnswer:
            print("")
            print(subAnswer, "is to low. Please try again.")
            print("")
            print(" ", sub1)
            print("-", sub2)
            subAnswer = int(input("Try again: "))
            attempts += 1

    # If subAnswer == correctSubAnswer Then
    #   Set attempts += 1
    #   Display ""
    #   Display "Attempts: ", attempts
    #   Display ""
    #   Display "Congradulations, ", subAnswer, "is correct."
    # End If
    if subAnswer == correctSubAnswer:
        attempts += 1
        print("")
        print("Attempts: ", attempts)
        print("")
        print("Congradulations, ", subAnswer, "is correct.")
    # End While
# End Function

# Function mainMenu()
def mainMenu():
    
    # Display ""
    # Display "Welcome to Math Quiz"
    # Display ""
    # Display ""
    # Display "MAINMENU"
    # Display "--------------------"
    # Display "1. Adding Random Numbers"
    # Display "2. Subtracting Random Numbers"
    # Display "3. Exit"
    # Display ""
    print("")
    print("Welcome to Math Quiz")
    print("")
    print("")
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print("")

    # Declare Integer user_input
    # Set user_input = Input
    # Input user_input
    user_input = int(input("Please choose one of the menu options: "))

    # If user_input <= 3 and user_input >= 1 Then
    if user_input <= 3 and user_input >= 1:
        # If user_input == 1 Then
        #   Call addingQuiz()
        #   Call mainMenu()
        # Else If user_input == 2 Then
        #   Call subtractingQuiz()
        #   Call mainMenu()
        # Else If user_input == 3 Then
        #   Display "Thank you for playing..."
        #   Display "Bye!!!"
        # End If
        if user_input == 1:
            addingQuiz()
            mainMenu()
        elif user_input == 2:
            subtractingQuiz()
            mainMenu()
        elif user_input == 3:
            print("Thank you for playing...")
            print("Bye!!!")
    # Else If user_input > 3 or user_input < 1 Then
    #   Display ""
    #   Display "Error please try again."
    #   Call mainMenu()
    # End If
    elif user_input > 3 or user_input < 1:
        print("")
        print("Error please try again.")
        mainMenu()

# Call mainMenu()
mainMenu()