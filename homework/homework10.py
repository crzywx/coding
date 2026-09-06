# ── GAME SETTINGS ──────────────────────────────────────────────
secret       = 27      # The hidden number the player must guess
max_attempts = 5

# ── SETUP ──────────────────────────────────────────────────────
count = 0
guess = 0
reamaining = 0

print("=" * 42)
print("        🎮  NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

while max_attempts > count and guess != 27:
    guess = int(input("Guess the secret number")
    max_attempts - 1
    count + 1
    print("❤️❤️❤️❤️")

    if guess==27:
        print("Well done! you guessed the number")
                elif guess >= 20:
                    print("Ice cold")
                elif guess >= 10:
                    print("Cold")
                elif guess >= 5:
                    print("Warm")
                else:
                    print("Hot")
remaining = max_attempts - count
if remaining > 0:
    print("❤️")
if guess != 27 and max_attempts < 0:
    print("Game over!")
                
                
    
# ── MAIN GAME LOOP ─────────────────────────────────────────────
# TODO: Write a while loop that keeps running as long as
#       count is less than max_attempts AND guess is not equal to secret

    # TODO: Read the player's guess using int(input())
    # TODO: Add 1 to count

    # TODO: If guess equals secret → print a win message

    # TODO: Otherwise (else):
    #   Calculate the distance (diff) between guess and secret
    #   WITHOUT using abs() — use an if/else instead

    #   Print a hint based on diff:
    #     diff >= 20  →  Ice cold
    #     diff >= 10  →  Cold
    #     diff >= 5   →  Warm
    #     else        →  Hot

    #   Calculate remaining = max_attempts - count
    #   If remaining > 0:
    #     Use a for loop to print a ❤️  for each remaining life

# ── GAME OVER CHECK ────────────────────────────────────────────
# TODO: After the loop, if guess is still not equal to secret
#       print a "Game over" message and reveal the secret number
