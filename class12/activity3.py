rows =int(input("Enter the number of rows"))
if rows%2==0:
    halfdiamondrow = rows//2
else:
    halfdiamondrow = rows//2+1
space = halfdiamondrow-1

for i in range(1,halfdiamondrow+1):
    for j in range(1, space+1):
        print(end=" ")
    space -= 1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num += 1
    print()
space = 1
for i in range(1 , halfdiamondrow):
        for j in range(1, space+1):
            print(end=" ")
        space = space+1
        num = 1 
        for j in range(1, 2*(halfdiamondrow-i)):
             print(end=str(num))
             num = num+1
        print()
