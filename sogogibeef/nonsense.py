# version : Jeong Min (sogogibeef)
# nonsense.py gets prompts user to type favorite word
# and prints it 12 times on a single line.
# then print the following string : "word doesn't even sound like a word anymore"


def repeat_12_times(word):
    list_of_words = [word] * 12
    # Note to self : no need to create blank lists as I did in java
    word_repeated = ' '.join(list_of_words)
    print(word_repeated)
    last_line = '"{}" doesn\'t even sound like a word anymore'.format(word)
    print(last_line)


favorite_word = input("Please type your favorite word: ")


repeat_12_times(favorite_word)
