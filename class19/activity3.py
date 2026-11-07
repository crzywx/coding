L = [4, 5, 1, 2, 9, 7, 10 , 8 ]
print("Original List:", L)

count = 0

for i in L:
    count += i

average = count / len(L)
print("Sum = ", count)
print("Average = ", average)

L.sort()

print("Smallest element is:", L[0])
print("Largest element is:", L[-1])