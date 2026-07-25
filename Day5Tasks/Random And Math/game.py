"""Create a Number Guessing Game where:
● The program generates a random number between 1 and 50 using random.
● The user has 5 attempts to guess the number.
● After each guess, calculate the absolute difference using math.fabs() and
display how far the guess is from the correct number."""

import random
import math

number = random.randint(1, 50)

print("You have 5 attempts.\n")

for i in range(5):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        difference = math.fabs(number - guess)
        print("Wrong guess!")
        print("You are", difference, "away from the correct number.")

if guess != number:
    print("\nGame Over!")
    print("The correct number was:", number)