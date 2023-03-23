'''created 2 functions one is the operator choice calculator the other
reads a file line by line and calculates the sum and displays the sum and answer'''

import os
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# user input sum operation and integer choices
def sum():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    with open("output.txt", "a") as f:

        while True:
    # take input from the user
            choice = input("Enter choice(1/2/3/4): ")
            
    # check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero")

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))
                    print(num1, "+", num2, "=", add(num1, num2), file=f)


                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))
                    print(num1, "-", num2, "=", subtract(num1, num2), file=f)

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))
                    print(num1, "*", num2, "=", multiply(num1, num2), file=f)

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                    print(num1, "/", num2, "=", divide(num1, num2), file=f)
        
        # check if user wants another calculation
        # break the while loop if answer is no
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation.lower() == "no":
                    break

# read from file function which asks user for the file and checks for it returns error if not found and tries again. 
# use list.txt as demo file with list              
def read_from_file():
    while True:    
        filename = input('What is the filename to access?\n')
        try:
            with open(filename) as fp:
                questions = fp.readlines() # reading the qustion file
        
                for q in questions:
                    Deleteequal = q.split('=')
                    a = eval(Deleteequal[0]) # always going to be line 0 because I am reading a line by line
                    f = q + str(a)
                    f = f.replace('\n', '') 
                    print(f)        
        except FileNotFoundError:
            print('The file that you are trying to open does not exist try again')
            #continue
        finally:
            try_again = input("Would you like to read another file? (yes/no): ") # loop to check if user wants to try another file
            if try_again.lower() == "no":
                    break
def choice():
    while True:
        user_choice = input('Do you want to input a sum or read from a file choose "read" or "sum" or "exit" to stop\n')   
        if user_choice == "sum":
            sum()
        elif user_choice == "read":
            read_from_file()
        elif user_choice == "exit":
            return
        else:
            print("Invalid choie")    


 # define main loop which contains the error loopbacks   
def main():
    try:
        choice()
    except ValueError as e:
        print(f"Error: {e}")
        choice()
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        choice()
    except Exception as e:
        print(f"Unexpected error: {e}")
        choice()
    finally:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Goodbye!")
   
main()





