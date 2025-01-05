"""
Simple Calculator Program
Author: Muhammad Zafar
Description: 
This is a beginner-friendly calculator program written in Python. 
It performs basic arithmetic operations (Addition, Subtraction, Multiplication, and Division) 
and allows users to perform multiple calculations in a loop until they choose to exit.

GitHub Repository: https://github.com/muhammadzafar9/Simple-Calculator
"""

def calculator():
    # Infinite loop to keep showing the menu until the user decides to exit
    while True:
        # Display the welcome message and menu
        print("\nWelcome to the Simple Calculator!")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        # Get the user's choice
        operation = input("Choose an operation (1/2/3/4/5): ")

        # Exit the program if the user selects option 5
        if operation == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        # Prompt the user to input two numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform the calculation based on the user's choice
        if operation == '1':
            print(f"The result is: {num1 + num2}")
        elif operation == '2':
            print(f"The result is: {num1 - num2}")
        elif operation == '3':
            print(f"The result is: {num1 * num2}")
        elif operation == '4':
            if num2 != 0:  # Check to avoid division by zero
                print(f"The result is: {num1 / num2}")
            else:
                print("Error! Division by zero is not allowed.")
        else:
            print("Invalid choice! Please select a valid operation.")

# Run the calculator function
calculator()
