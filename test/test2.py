#What you need to use
#------------------------------------------------------------------------
#1.  def and return     →  define 4 functions: add, subtract, multiply, divide
#2.  try/except         →  catch ZeroDivisionError and ValueError without crashing
#3.  float(input())     →  to read numbers from the user
#4.  return values      →  each function must return the correct result
#------------------------------------------------------------------------

def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b

choice = int(input("Enter choice (1-Add, 2-Subtract, 3-Multiply, 4-Divide): "))

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    
except ValueError:
    print("Invalid input! Please enter numeric values.")

if choice == 1:
    print("Result", add(num1, num2))
elif choice == 2:
    print("Result", subtract(num1, num2))
elif choice == 3:
    print("Result", multiply(num1, num2))
elif choice == 4:
    print("Result", divide(num1, num2))


 