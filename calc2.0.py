'''user is given a choice to do some enter an equation or read equations from a file, if user
chooses enter then it ask for the 2 numbers and the operator then calculates and outputs value to file
if user chooses read from file it will ask for filename and calculate the answers but doesnt write 
to a file.'''

import os.path
import os

#define functions
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

def write_equation_to_file(num1, num2, operator, result):
    with open("equations.txt", "a") as f:
        f.write(f"{num1} {operator} {num2} = {result}\n")

def read_equations_from_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError("File does not exist")
    with open(filename, "r") as f:
        equations = f.readlines()
    return equations

# main loop
while True:
    print("1. Enter an equation to solve")
    print("2. Read eqautions from frile to solve")
    print("3. to stop")
    choice = input("choice: ")
    if choice == "1":
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            result = calculate(num1, num2, operator)
            clear_screen()
            print(f"{num1} {operator} {num2} = {result}")
            write_equation_to_file(num1, num2, operator, result)
        except ZeroDivisionError as e:
            print(f"Error: {e}")    
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        try:
            filename = input("Enter the filename: ")
            equations = read_equations_from_file(filename)
            for equation in equations:
                equation = equation.split("=")[0]
                operators = ['*', '+', '-', '/']
                for operator in operators:
                    if operator in equation:
                        parts = equation.split(operator)
                        break
                num1 = eval(parts[0])
                num2 = eval(parts[1])
                result = calculate(num1, num2, operator)
                print(f"{equation} = {result}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
    elif choice == "3":
        clear_screen()
        print("Goodbye")
        break
    else:
        print("Invalid choice")
