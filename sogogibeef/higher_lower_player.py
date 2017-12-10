"""Jeong-Min Lim (@jeongm)
User is prompted to think of a number and program tries to guess.
Computer asks user how many guesses it would get, """

print('Think of a number between 1 and 100 and I\'ll guess it.')
guesses = int(input('How many guesses will I get? '))

answer_range = list(range(101))  # http://www.pythoncentral.io/pythons-range-function-explained/

while True:
    middle_value = sum(answer_range) // len(answer_range)
    if guesses == 0:
        ask_answer = input('I lost; what was the answer? ')
        if ask_answer in answer_range:
            answer_was_in_range = 'That can\'t be; you said it was higher than {}!'.format(middle_value)
            break
        print('Well played!')
        break


    middle_value_index = answer_range.index(middle_value)
    guess_prompt = 'Is the number higher, lower, or the same as {}? '.format(middle_value)
    value_comparison = input(guess_prompt)
    if value_comparison == 'same' and guesses != 0:
        print('I won!')
        break
    elif value_comparison == 'higher':
        answer_range = (answer_range[middle_value_index:])
    elif value_comparison == 'lower':
        answer_range = (answer_range[:middle_value_index - 1])
    guesses -= 1
