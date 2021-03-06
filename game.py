"""A number-guessing game."""

# Put your code here
import random

name = input("Hello. What's your name? ")
print("Hello {}".format(name))

secret_number = random.randrange(1, 101)

guess = "0"
num_guesses = 0

while(guess != secret_number):
	
	while True:

		guess = input("Guess a number between 1 and 100, inclusive: ")
		num_guesses += 1
		try:
			guess = int(guess)
			if guess == guess > 0 and guess == guess < 101:
				break
			else:
				print("Your guess must be between 1 and 100. Try again!")

		except ValueError:
			print("Your guess must be an integer. Try again!")
		
	
	if (guess == secret_number):
		print("Congrats you guess the secret number! And you only needed {} to do so!".format(num_guesses))
		break
	elif guess > secret_number:
		print("Your guess is too high! Try again!")
	else:
		print("Your guess is too low! Try again!")  