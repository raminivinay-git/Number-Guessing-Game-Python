#number guessing game

import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print()
print("------ PYTHON NUMBER GUESSING GAME ------")
print()
print(f"Select a number between {lowest_number} - {highest_number}")

while is_running:
    guess=input("Enter your guess: ")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print(f"Please select a number between {lowest_number} - {highest_number}")

        elif guess<answer:
            print("Too low! Try again.")

        elif guess>answer:
            print("Too high! Try again.")

        else:
            print(f"CORRECT. The Answer was {answer}")
            print(f"Number Of Guesses {guesses}")
            print()
            print("-----------------------------")
            is_running=False

    else:
        print("INVALID GUESS! Try Again")
        print(f"Please select a number between {lowest_number} - {highest_number}")
