operator_to_english = {'>': 'higher than',
                       '<': 'lower than',
                       '=': 'same as'}


def satisfies_comparison(operand1, operator, operand2):
    if operator == '>':
        return operand1 > operand2
    elif operator == '=':
        return operand1 == operand2
    elif operator == '<':
        return operand1 < operand2
    else:
        raise Exception('Invalid operator.')


def compatible_for_ints(condition1, condition2):
    operator1, operand1 = condition1
    operator2, operand2 = condition2
    return ((operator1 == operator2)
            or (operator1 == '>' and operator2 in ['=', '<']
                and operand1 + 1 < operand2)
            or (operator1 == '=' and operator2 in ['>', '<']
                and satisfies_comparison(operand1, operator2, operand2))
            or (operator1 == '<' and operator2 in ['>', '=']
                and operand1 > operand2 + 1))


minimum = 1
maximum = 100
print("Think of a number between {} and {} and I'll guess it.".format(
    minimum, maximum))

number_of_guesses = int(input('How many guesses do I get? '))
remaining_number_of_guesses = number_of_guesses
guess_correct = False
contradiction_found = False

conditions = []
initial_answer_range = range(minimum, maximum + 1)
answer_range = initial_answer_range

closing_sentence = 'Well played!'

while answer_range and remaining_number_of_guesses > 0 and not \
        guess_correct and not contradiction_found:
    remaining_number_of_guesses -= 1

    if len(answer_range) == 1:
        next_guess = answer_range[0]
    else:
        middle_number_index = int(len(answer_range) / 2)
        next_guess = answer_range[middle_number_index - 1]

    comparison = input(
        'Is the number higher, lower, or the same as {}? '.format(next_guess))
    comparison_formatted = comparison.strip().lower()
    if 'low' in comparison_formatted:
        operator = '<'
    elif 'high' in comparison_formatted:
        operator = '>'
    elif 'same' in comparison_formatted:
        operator = '='
        guess_correct = True
    else:
        raise Exception('Invalid input.')

    new_condition = operator, next_guess
    conditions.append(new_condition)

    for previous_condition in conditions:
        if compatible_for_ints(previous_condition, new_condition):
            answer_range = [number for number in answer_range if
                            satisfies_comparison(number, operator, next_guess)]
        else:
            contradiction_found = True
            previous_condition_operator = previous_condition[0]
            previous_condition_operand = previous_condition[1]
            previous_condition_operator_in_english = operator_to_english.get(
                previous_condition_operator)
            new_condition_operator = new_condition[0]
            new_condition_operand = new_condition[1]
            new_condition_operator_in_english = operator_to_english.get(
                new_condition_operator)
            closing_sentence = 'Wait; how can it be both {} {} and {} {}?'.format(
                previous_condition_operator_in_english,
                previous_condition_operand,
                new_condition_operator_in_english, new_condition_operand)
            break

if contradiction_found:
    pass  # already changed the closing sentence beforehand
elif guess_correct:
    closing_sentence = 'I won!'
elif not answer_range or remaining_number_of_guesses == 0:
    answer = int(input('I lost; what was the answer? '))
    if answer not in initial_answer_range:
        closing_sentence = "I said it was between {} and {}!".format(minimum,
                                                                     maximum)
    else:
        for condition in conditions:
            condition_operator, condition_operand = condition
            if not satisfies_comparison(answer, condition_operator,
                                        condition_operand):
                condition_operator_in_english = operator_to_english.get(
                    condition_operator)
                closing_sentence = "That can't be; you said it was {} {}!".format(
                    condition_operator_in_english, condition_operand)
                break

print(closing_sentence)
