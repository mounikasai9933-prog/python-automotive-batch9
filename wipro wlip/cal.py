def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b


# Main Program
print("----- Calculator Menu -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print("Addition:", add(num1, num2))

elif choice == 2:
    print("Subtraction:", sub(num1, num2))

elif choice == 3:
    print("Multiplication:", mul(num1, num2))

elif choice == 4:
    print("Division:", div(num1, num2))

else:
    print("Invalid choice")