"""A number-guessing game."""

# Put your code here
import random

name = input("Hello. What's your name? ")
print("Hello {}".format(name))

secret_number = random.randrange(1, 101)
print(secret_number)

guess = 0
num_guesses = 0

while(guess != secret_number):
	guess = int(input("Guess a number between 1 and 100, inclusive: "))
	num_guesses += 1
	
	if (guess == secret_number):
		print("Congrats you guess the secret number! And you only needed {} to do so!".format(num_guesses))
		break

	elif guess > secret_number:
		print("Your guess is too high! Try again")

	else:
		print("Your guess is too low! Try again!")  

