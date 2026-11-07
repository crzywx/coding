# ================================
# FUNCTION CALCULATOR
# ================================

# ---------- PART 1: four functions ----------
# YOUR CODE HERE
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Write add(a, b), subtract(a, b), multiply(a, b) and divide(a, b).
# Each one should return its answer. Do not print inside the functions.

# ---------- MAIN PROGRAM (given to you) ----------
print("FUNCTION CALCULATOR")

# ---------- PART 2, 3 and 4: input, choose, errors ----------
# YOUR CODE HERE
try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Enter an operation (add, subtract, multiply, divide): ").strip().lower()

    if operation == "add":
        print(add(first_number, second_number))
    elif operation == "subtract":
        print(subtract(first_number, second_number))
    elif operation == "multiply":
        print(multiply(first_number, second_number))
    elif operation == "divide":
        print(divide(first_number, second_number))
    else:
        print("Unknown operation.")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Thank you for using the function calculator!")
