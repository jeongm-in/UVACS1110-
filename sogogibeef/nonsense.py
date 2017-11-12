# version : Jeong Min (sogogibeef)
# nonsense.py gets prompts user to type favorite word
# and prints it 12 times on a single line.
# then print the following string : "word doesn't even sound like a word anymore"


def repeat_12_times(word):
    list_of_words = [word] * 12 # Following bartleby's advice, removed unnecessary iteration
    word_repeated = ' '.join(list_of_words)
    print(word_repeated)
    print(('\"%s\" doesn\'t even sound like a word anymore') % word)
    # Following bartleby's advice, used %s string formatter instead of messy escape sequences


favorite_word = input("Please type your favorite word: ")
# I am so used to initializing variables. Perhaps (at least for me) biggest difference
# Q : for long comments, what should I do? break to the next line?

repeat_12_times(favorite_word)
