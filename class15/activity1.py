def bill(amt,tip):
    total = amt + tip/100 * amt
    return total

print(f"Your total amount is {bill(tip=20,amt=50)}")