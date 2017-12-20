user_input = input('Enter an integer: ')
while not 0 < int(user_input) < 4000:
    print('Input must be between 1 and 3999')
    user_input = input('Enter an integer: ')

symbols = 'IVXLCDM'
answer = ''
for i in range(len(user_input)):
    digit = int(user_input[-i - 1])
    if digit % 5 == 4:
        chunk = symbols[2 * i] + symbols[2 * i + (digit // 5) + 1]
    elif digit >= 5:
        chunk = symbols[2 * i + 1] * (digit // 5) + symbols[2 * i] * (digit % 5)
    else:
        chunk = symbols[2 * i] * (digit % 5)
    answer = chunk + answer

print('In roman numerals, {} is {}'.format(user_input, answer))
