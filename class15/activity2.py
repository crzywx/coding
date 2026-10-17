def cube(amount):
    return amount**3

def div_3(amount):
    if amount % 3 == 0:
        return cube(amount)
    else:
        return "the number is not divisible by 3"
print(div_3(10))
print(div_3(33))