# Version : Jeong Min Lim (sogogibeef)
# calculator.py contains function binop that evaluates string containing
# simple arithmetic expressions
# Thought question 1  complete
# Very poor extraction
# Thought question 2 Wip
# TODO: for negative numbers, how to determine which - sign is an operator, not negative sign?
# Thought question 3 WIP


def binop(arithmetic_expression):
    # Accepted operators : +, -, *, /
    operators = "-+*/"
    operators_other_than_subtract = operators[:-1]
    operator_other_than_subtract_is_in_expression = [True for operator in operators_other_than_subtract
                                                     if operator in arithmetic_expression]
    # Check if expression is only consisted of operators other than - (Basis for TQ3)
    # But if expression is something like 3 * -5 - - 10, then this whole thing goes to wreck
    # HOW to tell the difference of - and -???????????????
    # TQ3 surely is difficult!

    if any(operator_other_than_subtract_is_in_expression):
        for operator in operators_other_than_subtract:

            if operator in arithmetic_expression:
                operands = arithmetic_expression.split(operator)
                operand1 = int(operands[0])
                operand2 = int(operands[1])

                if operator == "+":
                    return operand1 + operand2

                elif operator == "*":
                    return operand1 * operand2

                elif operator == "/":
                    return operand1 / operand2

    elif '-' in arithmetic_expression:
        stripped_expression = arithmetic_expression.strip()
        # 0. -A : only one -sign and - sign at 0. But can just return whole expression to deal with A
        # 1. A - B : only one - sign and - sign not at 0
        # 2. -A - B : two - signs and -sign at 0
        # 3. A - -B : two - signs and -sign not at 0
        # 4. -A - -B : three - signs and -sign at 0

        if stripped_expression:
            return None # WIP








print(binop("-111 * -10"))
print(binop("    -11+11     "))
print(binop("131 / -11"))
print(binop("   965   -      123"))
print(binop("    1111     "))

