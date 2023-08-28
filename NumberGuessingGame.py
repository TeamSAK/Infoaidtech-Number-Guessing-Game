# Number Guessing Game
import random

def main():
    print("Welcome to the Number Guessing Game!")
    player_name = input("What's your name? ")
    print(f"Hi, {player_name}! You have 10 attempts to guess the number between 1 and 100.")

    while True:
        random_number = random.randint(1, 100)
        attempts = 0

        while attempts < 10:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                print(f"Congratulations, {player_name}! You guessed the number {random_number} correctly in {attempts} attempts.")
                break

        if guess != random_number:
            print(f"Sorry, {player_name}. You've used all your attempts. The number was {random_number}.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
