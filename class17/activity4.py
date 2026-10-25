try:
    n = int(input("Enter a number: "))
    while n % 2 == 0:
        print("n is an integer")
except ValueError:
    print("n is not an integer")
