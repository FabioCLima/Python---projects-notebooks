"""
Writw a Python program to guess a number between 1 to 9
User is prompted to enter a guess. If the user 
guesses wrong then the prompt appears again until 
the guess is correct, on successful guess, user
will get a "Well guessed!"
"""
import random
target_num, guess_num = random.randint(1, 10), 0

while target_num != guess_num:
    guess_num = input("Guess a number between 1 and 9 \n")

    if not guess_num.isnumeric():
        print("Guess a valid number between 1 and 9")
    else:
        guess_num = int(guess_num)
print("Well guessed!")
