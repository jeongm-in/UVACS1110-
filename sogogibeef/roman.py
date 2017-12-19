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
        # print(denominator)
        how_many_roman_numerals = divmod(arabic_numeral, denominator)
        for num in range(how_many_roman_numerals[0]):
            roman_numeric_list.append(roman_dictionary[denominator])
        arabic_numeral = how_many_roman_numerals[1]  # #15

    roman_numeric_result = ''.join(roman_numeric_list)
    print(roman_numeric_result)
