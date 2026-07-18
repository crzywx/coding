#the mean of 40 numbers is 38

#later on it is detected that i misread

#56 as 36. Find the corrected mean

n = 40
mean1 = 38
wrong_number = 36
right_number = 56
sum1 = mean1 * n
print("The incorrect sum was ", sum1)

sum2 = sum1 - (wrong_number - right_number)
mean2 = sum2 / n
print("The corrected mean is", mean2)
