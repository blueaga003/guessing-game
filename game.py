"""A number-guessing game."""

# Put your code here
import random

name = input("Hello. What's your name? ")
print("Hello {}".format(name))

secret_number = random.randrange(1, 101)
print(secret_number)

guess = int(input("Guess a number between 1 and 100, inclusive: "))
