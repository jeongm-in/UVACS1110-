# Ask user which number to use for guessing game (integer between 1 and 100)
# If user inputs -1, Computer will pick a number between 1 and 100
# User is prompted to set how many guesses user would get

import random

user_input_is_valid = False

while True:
    user_answer = int(input('What should the answer be? '))
    if user_answer == -1:
        answer = random.randrange(1, 101)
        break
    elif user_answer in range(1, 101):
        answer = user_answer
        break
    print('Type number between 1 and 100 or -1 for random answer.')

guesses_remaining = int(input('How many guesses? '))
is_answer = False

while is_answer == False:
    guess = int(input('Guess a number: '))
    guesses_remaining -= 1
    if guesses_remaining == 0 and guess != answer:
        lose_message = 'You lose; the number was {}.'.format(answer)
        print(lose_message)
        break
    elif guess < answer:
        print('The number is higher than that.')
    elif guess > answer:
        print('The number is lower than that.')
    else:
        print('You win!')
        break
