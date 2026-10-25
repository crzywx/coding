import random 
playing = True
number = str(random.randint(0, 9))
print("I will generate a random number from 0 to 9 , try to guess it")
print("The game ends when you guess the correct answer")
while playing:
    guess = input("Give me your best guess \n")
    if guess == number:
        print("Correct guess!")
        print("The number was ", number)
        break

    else: 
        print("This isn't the right guess, try again")