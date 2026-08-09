total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
total_dispensed = 0 

serving = True
while serving:
    customer_name = input("Enter the customers name")
    amount = int(input(f"{customer_name}, please enter the amount you want to withdraw"))
    if amount <= 0:
        print("Invalid amount.")
        continue

    print(f"We are dispensing {amount} for {customer_name}")
    remaining = amount
    idx = 1
    while idx<=6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        elif idx == 6: value = 1
        count = remaining // value
        if count > 0:
            print(f"{count} * {value}- notes = {count} * {value}")
            remaining -= count * value
            if value == 100: total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count
            elif value == 1: total_1 += count
        idx +=1

    customers_served += 1
    total_dispensed += amount
    print(f"Transaction is complete, {customer_name}")
    next_customer = input("Is there a next customer? (yes/no)").strip().lower()
    if next_customer != "yes":
        serve = False

            
            



        

 
    

