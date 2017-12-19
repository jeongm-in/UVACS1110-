# jeongm(limjeongmin@wustl.edu)
# prompts user to enter an integer between 0 and 4000, and returns roman numeral of user input
# input must be an integer between 0 and 4000
roman_dictionary = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

upper_limit = 4000
lower_limit = 0
roman_numeric_list = []

arabic_numeral = int(input('Enter an integer: '))
if arabic_numeral <= lower_limit or arabic_numeral >= upper_limit:
    print('Input must be between 1 and 3999.')

else:
    for denominator in roman_dictionary.keys():
        how_many_roman_numerals = divmod(arabic_numeral, denominator)
        for num in range(how_many_roman_numerals[0]):
            roman_numeric_list.append(roman_dictionary[denominator])
        arabic_numeral = how_many_roman_numerals[1]  # #15

    roman_numeric_joined = ''.join(roman_numeric_list)

# Fix roman numerics in proper format
# TODO : how to extract if bulk for formatting
if 'DCCCC' in roman_numeric_joined:
    roman_numeric_joined = roman_numeric_joined.replace('DCCCC', 'CM')
if 'D' not in roman_numeric_joined and 'CCCC' in roman_numeric_joined:
    roman_numeric_joined = roman_numeric_joined.replace('CCCC', 'CD')
if 'LXXXX' in roman_numeric_joined:
    roman_numeric_joined = roman_numeric_joined.replace('LXXXX', 'XC')
if 'L' not in roman_numeric_joined and 'XXXX' in roman_numeric_joined:
    roman_numeric_joined = roman_numeric_joined.replace('XXXX', 'XL')
if 'VIIII' in roman_numeric_joined:
    roman_numeric_joined = roman_numeric_joined.replace('VIIII', 'IX')
if 'V' not in roman_numeric_joined and 'IIII' in roman_numeric_joined:
    roman_numeric_joined = roman_numeric_joined.replace('IIII', 'IV')

print(roman_numeric_joined)
