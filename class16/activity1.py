import random


def play_car_game():
    """Play a simple text-based car racing game."""
    finish = 30
    distance = 0
    fuel = 10

    print("Welcome to Car Race!")
    print("Reach 30 miles before you run out of fuel.")
    print("Press Enter to drive, or type q to quit.")

    while distance < finish and fuel > 0:
        print(f"\nDistance: {distance}/{finish} | Fuel: {fuel}")
        print("=" * distance + "🚗" + "-" * (finish - distance))
        command = input("> ").strip().lower()

        if command == "q":
            print("Race quit. See you next time!")
            return
        if command not in ("", "drive"):
            print("Type 'drive', press Enter, or type 'q'.")
            continue

        fuel -= 1
        distance += random.randint(3, 6)
        if random.random() < 0.2:
            distance -= 2
            print("You hit traffic and lost some distance!")
        distance = max(0, distance)

    if distance >= finish:
        print("\n🏁 You made it to the finish line. You win!")
    else:
        print("\nYou ran out of fuel. Game over!")


if __name__ == "__main__":
    play_car_game()