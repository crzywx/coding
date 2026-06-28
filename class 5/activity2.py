sp = int(input("Enter your sale price"))
cp = int(input("Enter your cost price"))
if sp > cp:
    print("your profit is", sp - cp)
else:
    print("You're in debt")