def greeting():
    print("Welcome to my lemonade stand!")

greeting()

num_cup = int(input("How many cups would you like?"))
cup_cost = float(input("How much is each cup?"))

def total_cost(cup, cost):
    total=cup*cost
    return total

total=total_cost(num_cup , cup_cost)

rounded_total = round(total, 2)
print(f"Your total is £{rounded_total}")

amount_paid = float(input("Enter the amount paid"))

def change(amount, paid):
    change=paid-amount
    return change

change_needed=change(rounded_total, amount_paid)
change_needed=round(change_needed, 2)

def thanks(cups):
    if cups >= 5:
        return("Thank you for such a big order!")
    else:
        return("Thanks for the support")
closing_message=thanks(num_cup)

print("")
print("LEMONADE STAND RECEIPT")
print("price per cup:", cup_cost)
print("cup sold:", num_cup)
print("total cost:", rounded_total)
print("amount paid:", amount_paid)
print("change due:", change_needed)
print(closing_message)

