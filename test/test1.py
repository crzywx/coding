random = 28
lives = 5
while lives > 0:
    guess = int(input("Guess the number: "))
    if guess == random:
        print("You've guessed the right answer!")
        break
    elif guess // 10 == 2:
        print("Hot!!")
    
  
