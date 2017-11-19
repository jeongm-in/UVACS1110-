# Version : Jeong Min Lim (sogogibeef)
# calculator.py contains function binop that evaluates string containing
# simple arithmetic expressions
# Thought question 1  complete
# Thought question 2 Wip
# TODO: for negative numbers, how to determine which - sign is an operator, not negative sign?
# Thought question 3 WIP

def binop(arithmetic_expression):
    # Accepted operators : +, -, *, /
    if "+" in arithmetic_expression:
        list_of_numbers = arithmetic_expression.split("+")
        result = int(list_of_numbers[0]) + int(list_of_numbers[1])
        return result

    elif "-" in arithmetic_expression:
        list_of_numbers = arithmetic_expression.split("-")
        if int(list_of_numbers[-1]) < 0:
            return sum(list_of_numbers)
        result = int(list_of_numbers[0]) - int(list_of_numbers[1])
        return result

    elif "*" in arithmetic_expression:
        list_of_numbers = arithmetic_expression.split("*")
        result = int(list_of_numbers[0]) * int(list_of_numbers[1])
        return result

    elif "/" in arithmetic_expression:
        list_of_numbers = arithmetic_expression.split("/")
        result = int(list_of_numbers[0]) / int(list_of_numbers[1])
        return result

    elif "+" or "-" or "/" or "*" not in arithmetic_expression:
        return arithmetic_expression


