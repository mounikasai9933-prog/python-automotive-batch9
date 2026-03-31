def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Sequence of calculator events using range
for step in range(1, 6):   # Calculator runs 5 times
    print("\nCalculator Step:", step)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", sub(num1, num2))
    elif choice == 3:
        print("Result:", mul(num1, num2))
    elif choice == 4:
        print("Result:", div(num1, num2))
    else:
        print("Invalid choice")