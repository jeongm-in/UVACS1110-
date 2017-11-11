# version : Jeong Min (sogogibeef)
# nonsense.py gets prompts user to type favorite word
# and prints it 12 times on a single line.
# then print the following string : "word doesn't even sound like a word anymore"


def repeat_12_Times(word):
    list_of_words = [''] * 12
    for i in range(12):
        list_of_words[i] = word
    word_repeated = ' '.join(list_of_words)
    print(word_repeated)

    print(('\'%s\' doesn\'t even sound like a word anymore') % word)
    # following bartleby's advice, used %s string formatter instead of messy escape sequences


favorite_word = input("Please type your favorite word: ")
# I am so used to initializing variables. Perhaps (at least for me) biggest difference
# Q : for long comments, what should I do? break to the next line?

repeat_12_Times(favorite_word)
