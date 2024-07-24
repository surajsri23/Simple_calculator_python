import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def logarithm(x):
    if x > 0:
        return math.log(x)
    else:
        return "Error! Logarithm of non-positive number."

def percentage(x, y):
    return (x * y) / 100

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Logarithm")
    print("6. Percentage")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")

            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")

            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")

            elif choice == '6':
                print(f"The result is: {percentage(num1, num2)}")

        elif choice == '5':
            num = float(input("Enter number: "))
            print(f"The result is: {logarithm(num)}")

        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
