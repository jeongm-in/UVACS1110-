# Version : Jeong-Min Lim(sogogibeef)
# rumple.py prompts user to guess correct name.

is_correct_guess = False
answer = 'Rumpelstiltskin'
print('You will never win the game, for Rumpelstiltskin is my name.')
guesses = 0

while is_correct_guess == False:
    if guesses == 500:  # TQ1: limit number of guesses
        break
    user_answer = input('Guess my name: ')
    if user_answer == answer:
        break  #
    elif user_answer != '':  # TQ2: Not to gloat when user inputs nothing
        print('Ha! You\'ll never guess!')
    guesses += 1

if guesses < 500:
    print('No! How did you guess?')
else:
    print('I told you couldn\'t guess!')
