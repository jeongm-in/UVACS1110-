mistakes = 0
game_over = False
answer = input('Enter a phrase: ').lower()
portion_guessed = '_'.join(answer) + '_'
portion_guessed = portion_guessed.replace(' _', '  ').replace('-_', '--')
portion_guessed = portion_guessed.replace('._', '..').replace(',_', ',,')
portion_guessed = portion_guessed.replace('?_', '??').replace('!_', '!!')
portion_guessed = portion_guessed.replace(';_', ';;').replace(':_', '::')
portion_guessed = portion_guessed.replace("'_", "''").replace('"_', '""')
current = portion_guessed[1::2]
print('Phrase to guess: ' + current)
letter = input('Guess a letter: ')  # no while, so no verification
if letter + '_' in portion_guessed:
    print("There is a '{}'!".format(letter))
    portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
else:
    mistakes += 1
    print("Nope; that's mistake number {}".format(mistakes))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))

current = portion_guessed[1::2]
if not game_over:
    if '_' in portion_guessed and mistakes < 6:
        print('Phrase to guess: ' + current)
        letter = input('Guess a letter: ')
        if letter + '_' in portion_guessed:
            print("There is a '{}'!".format(letter))
            portion_guessed = portion_guessed.replace(letter + '_', letter * 2)
        else:
            mistakes += 1
            print("Nope; that's mistake number {}".format(mistakes))
    else:
        game_over = True
        if '_' not in portion_guessed:
            print('You win!')
        else:
            print('You lose!')
            print('You guessed    "{}"'.format(current))
        print('The answer was "{}"'.format(answer))
