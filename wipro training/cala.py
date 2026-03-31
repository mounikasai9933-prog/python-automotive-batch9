def add(a, b):
    return a + b

# Subtraction function
def sub(a, b):
    return a - b

# Multiplication function
def mul(a, b):
    return a * b

# Division function
def div(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b


# -------- Main Program --------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))