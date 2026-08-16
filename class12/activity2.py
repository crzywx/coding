row = int(input("Enter the number of rows: "))
num = 1
for i in range(1, row+1):
    for j in range(i):
        print(num, end="\t")
        num+=1
    print()

