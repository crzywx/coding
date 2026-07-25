print("Welcome to Ride Builder")

print("Step1: Pick your vehicle")
print("1- bike")
print("2- car")

choice = int(input("Choose 1 or 2:  "))

if choice == 1:
    print("Step 2: pick your bike")
    print("1- motorbike")
    print("2- mountain bike")

    bike_type = int(input("Enter 1 or 2: "))

    if bike_type == 1:
        print("You chose - motorbike")
        print("Top Speed - 120mph")
        print("Best for - highway")

    else:
        print("You chose - mountainbike")
        print("Top Speed - 40mph")
        print("Best for - offroad ")
    
elif choice == 2:
    print("Step 2: pick your car")
    print("1- honda")
    print("2- mercedes")

    bike_type = int(input("Enter 1 or 2: "))

    if bike_type == 1:
        print("You chose - honda")
        print("Top Speed - 120mph")
        print("Best for - city")

    else:
        print("You chose - mercedes")
        print("Top Speed - 160mph")
        print("Best for - highway ")

else:
    print("Invalid")

print("Your custom ride is completed, enjoy!")



