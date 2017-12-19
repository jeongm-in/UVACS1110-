class Condition(object):
    def __init__(self, operator, operand):
        assert operator and operator in '>=<', \
            "Parameter 'operator' must be one of '>', '=', or '<'."
        assert isinstance(operand, int), \
            "Parameter 'operand' must be an int."
        self.operator = operator
        self.operand = operand

    def compatible_with(self, another_condition):
        assert isinstance(another_condition, Condition), \
            "Parameter 'condition' must be a Condition"
        operator1 = self.operator
        operand1 = self.operand
        operator2 = another_condition.operator
        return ((operator1 == '>' and operator2 in '=<'
                 and another_condition.satisfied_by(operand1 + 1))
                or (operator1 == '=' and operator2 in '>=<'
                    and another_condition.satisfied_by(operand1))
                or (operator1 == '<' and operator2 in '>='
                    and another_condition.satisfied_by(operand1 - 1))
                or operator1 == operator2 and operator2 in '><')

    def satisfied_by(self, number):
        assert isinstance(number, int), \
            "Parameter 'number' must be an int."
        if self.operator == '=':
            return self.operand == number
        else:
            return eval('{}{}{}'.format(number, self.operator, self.operand))


operator_to_english = {'>': 'higher than',
                       '<': 'lower than',
                       '=': 'same as'}

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

    new_condition = Condition(operator, next_guess)
    conditions.append(new_condition)

    for previous_condition in conditions:
        if previous_condition.compatible_with(new_condition):
            answer_range = [number for number in answer_range if
                            new_condition.satisfied_by(number)]
        else:
            contradiction_found = True
            previous_condition_operator_in_english = operator_to_english.get(
                previous_condition.operator)
            new_condition_operator_in_english = operator_to_english.get(
                new_condition.operator)
            closing_sentence = 'Wait; how can it be both {} {} and {} {}?'.format(
                previous_condition_operator_in_english,
                previous_condition.operand,
                new_condition_operator_in_english, new_condition.operand)
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
            if not condition.satisfied_by(answer):
                condition_operator_in_english = operator_to_english.get(
                    condition.operator)
                closing_sentence = "That can't be; you said it was {} {}!".format(
                    condition_operator_in_english, condition.operand)
                break

print(closing_sentence)
