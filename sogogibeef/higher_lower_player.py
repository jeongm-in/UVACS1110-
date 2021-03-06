"""Jeong-Min Lim (@jeongm)
# User is prompted to think of a number and program tries to guess.
# Computer asks user how many guesses it would get, """
#
# print('Think of a number between 1 and 100 and I\'ll guess it.')
# guesses = int(input('How many guesses will I get? '))
#
# answer_range = list(range(101))  # http://www.pythoncentral.io/pythons-range-function-explained/
#
# while True:
#     middle_value = sum(answer_range) // len(answer_range)
#     # end condition -> use switches
#     middle_value_index = answer_range.index(middle_value)
#     guess_prompt = 'Is the number higher, lower, or the same as {}? '.format(middle_value)
#     value_comparison_raw = input(guess_prompt)
#     value_comparison = value_comparison_raw.strip().lower()  # TQ
#     if value_comparison == 'higher':
#         answer_range = (answer_range[middle_value_index:])
#     elif value_comparison == 'lower':
#         answer_range = (answer_range[:middle_value_index - 1])
#     # End conditions
#
#     final_max = answer_range[-1]
#     final_min = answer_range[0]
#
#     if guesses == 0 and value_comparison != 'same':
#         user_answer = int(input('I lost; what was the answer? '))
#         if user_answer <= final_min:
#             user_lied_higher = 'That can\'t be; you said it was higher than {}!'.format(final_min)
#             print(user_lied_higher)
#             break
#         elif user_answer >= final_max:
#             user_lied_lower = 'That can\'t be; you said it was lower than {}!'.format(final_max)
#             print(user_lied_lower)
#             break
#         else:
#             print('Well played!')
#             break
#     elif len(answer_range) == 0:
#         answer_out_of_range = 'Wait; how can it be both higher than {} and lower than {}?'.format(final_min,
#                                                                                                   final_max)
#         print(answer_out_of_range)
#         break
#     elif value_comparison == 'same':
#         print('I won!')
#         break
#
#     guesses -= 1


print("Think  of a number between 1 and 100 and I'll guess it.")
guesses_remaining = int(input('How many guesses do I get? '))
answer_range = list(range(1, 101))

while (True):
    middle_value_index = (len(answer_range) - 1) // 2
    middle_value = answer_range[middle_value_index]
    answer_prompt = 'Is the number higher, lower, or the same as {}? '
    raw_user_input = input(answer_prompt.format(middle_value))

    if 'high' in raw_user_input:
        user_input = 'higher'
    elif 'low' in raw_user_input:
        user_input = 'lower'
    elif 'same' in raw_user_input:
        user_input = 'same'

    max_answer_range = answer_range[-1]
    min_answer_range = answer_range[0]

    guesses_remaining -= 1

    if guesses_remaining == 0:
        intended_answer = int(input('I lost; what was the answer? '))
        answer_out_of_range = "That can't be; you said it was {} than {}!"
        if intended_answer < min_answer_range:
            print(answer_out_of_range.format('lower', min_answer_range))
            break
        elif intended_answer > max_answer_range:
            print(answer_out_of_range.format('higher', max_answer_range))
            break
        else:
            print('Well played!')
            break

    if user_input == 'higher':
        answer_range = answer_range[middle_value_index:]
    elif user_input == 'lower':
        answer_range = answer_range[:middle_value_index]
    elif user_input == 'same':
        print('I won!')
        break
