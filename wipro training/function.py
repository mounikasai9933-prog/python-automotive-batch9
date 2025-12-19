ef add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Marks Function
def check_result(marks):
    if marks > 60:
        return "PASS"
    else:
        return "FAIL"

# Main Program
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", add(x, y))
print("Subtraction:", sub(x, y))
print("Multiplication:", mul(x, y))
print("Division:", div(x, y))

m = int(input("Enter marks: "))
print("Result:", check_result(m