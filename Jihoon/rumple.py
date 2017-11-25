number_of_guesses = 0
limit = 5  # TQ1: limit the number of guesses that can be made
name = 'Rumpelstiltskin'
guess_correct = False

prompt = 'You will never win the game, for {} is my name.'.format(name)
print(prompt)

while not guess_correct and number_of_guesses < limit:
    guess = ''
    while guess == '':  # keep asking as long as the input is empty
        # TQ2: If the user types nothing, it might be nicer not to gloat
        guess = input('Guess my name: ')

    number_of_guesses += 1
    if guess == name:
        guess_correct = True
        break
    else:
        print("Ha! You'll never guess!")

if guess_correct:
    print('No! How did you guess?')
elif number_of_guesses >= limit:
    print('No more guesses!')
