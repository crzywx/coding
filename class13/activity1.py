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
