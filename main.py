"""
Number guessing game.
"""
# Import random module to generate a random number
import random

# Function to get a valid integer input with error handling

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please eneter a valid integer.")

def yes_or_no(prompt):
    while True:
        replay = input(prompt).lower()

        if replay in ["y", "n"]:
            return replay
        else:
            print("Please enter 'y' or 'n'")

def number_guessing_game() -> None:
    while True:
        lowest = get_valid_integer("Please type the lowest number to guess. ")

        highest = get_valid_integer("Please type the highest number to guess. ")

        if lowest < highest:
            break

        else:
            print("The lowest number should be less than the highest number.")

    #whatever

    

    max_attempts = get_valid_integer("How many attempts do you want? ")
    while max_attempts <= 0:
        print("Please print a positive inetger.")
        max_attempts = get_valid_integer("Enter the number of attempts you want.")

    real_number = random.randint(lowest, highest)

    attempts = 0

    while attempts < max_attempts:
        guess = get_valid_integer(
            f"Attempt {attempts + 1}/{max_attempts}: Enter your guess. "
        )
        attempts += 1

        if guess < real_number:
                print("Too low! Try again.")

        elif guess > real_number:
                print("Too high! Try again.")
                
        elif guess == real_number:
                print(f"Yay! You got the number in {attempts} attempts!")

                break
           
    

def main():

    print("Hello user! Welcome to Genious Abby's number guessing game.")

    name = input("Please type your name here. ")

    print(f"Welcome, {name}!")

    while True:
        number_guessing_game()
        play_again = yes_or_no("Would you like to play again? (y/n): ")
        if play_again == 'n':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

# Function to get a valid 'y' or 'n' response from the user
 

# Function to play one round of the game


# Ask for number range


# Ensure low_number is less than high_number


# Ask for number of attempts


# Generate random number


# Track number of attempts


# Loop for user guesses


# Check if guess is too low or too high


# Display success message if guessed correctly


# If max attempts are used up, reveal the correct number


# Main game loop


# Ask for user's name and greet them


# Ask if they want to play again, only accepting 'y' or 'n'


# Run the game
