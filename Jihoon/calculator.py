def binop(expression):
    """accepts a single string parameter consisting of two positive integers and
     a singe operator between them, where the operator is one of +, -, *, or /.
     There may also be arbitrarily many spaces before or after either number and
     /or the operator. The function returns the int or float value created by
     evaluating the expression."""
    operators = ['+', '-', '*', '/']
    operator_found = False
    for operator in operators:
        if operator_found:
            break
        else:
            if operator in expression:
                operator_found = True
                expression_in_list = expression.split(operator)
                operand1 = int(expression_in_list[0])
                operand2 = int(expression_in_list[1])
                if operator == '+':
                    return operand1 + operand2
                elif operator == '-':
                    return operand1 - operand2
                elif operator == '*':
                    return operand1 * operand2
                else:
                    return operand1 / operand2
