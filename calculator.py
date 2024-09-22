def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operation = input("What operation do you want to do (addition, subtraction, multiplication, division): ").lower()

if operation == "addition":
    print(f"The addition of {num1} and {num2} is: {add(num1, num2)}")

elif operation == "subtraction":
    print(f"The subtraction of {num1} and {num2} is: {subtract(num1, num2)}")

elif operation == "multiplication":
    print(f"The multiplication of {num1} and {num2} is: {multiply(num1, num2)}")

elif operation == "division":
    print(f"The division of {num1} and {num2} is: {divide(num1, num2)}")

else:
    print("Error: Invalid operation.")
