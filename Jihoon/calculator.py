def binop(expression):
    """accepts a single string parameter consisting of two positive integers and
     a singe operator between them, where the operator is one of +, -, *, or /.
     There may also be arbitrarily many spaces before or after either number and
     /or the operator. The function returns the int or float value created by
     evaluating the expression."""
    operators = '+-*/'
    for i, character in enumerate(expression):
        if character == '+':
            return binop(expression[:i]) + binop(expression[i + 1:])
        elif character == '-':
            # first character or preceded by an operator -> negative number
            if i == 0 or expression[i - 1] in operators:
                continue
            else:
                # if the previous character is a number -> subtraction
                return binop(expression[:i]) - binop(expression[i + 1:])
        elif character == '*':
            return binop(expression[:i]) * binop(expression[i + 1:])
        elif character == '/':
            return binop(expression[:i]) / binop(expression[i + 1:])

    if expression.strip() == '':
        return 0
    else:
        return int(expression)
