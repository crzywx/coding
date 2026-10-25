try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("The answer is ", result)

except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("You must enter a whole number")
except:
    print("Wrong input")
else:
    print("No exception")
finally:
    print("This will print no matter what")