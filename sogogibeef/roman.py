# jeongm(limjeongmin@wustl.edu)
# prompts user to enter an integer between 0 and 4000, and returns roman numeral of user input
# input must be an integer between 0 and 4000
roman_dictionary = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
limit_upper_lower = [0, 4000]
RN_list = []
arabic_numeral = int(input('Enter an integer: '))
if arabic_numeral <= limit_upper_lower[0] or arabic_numeral >= limit_upper_lower[1]:
    print('Input must be between 1 and 3999.')
else:
    for denominator in roman_dictionary.keys():
        how_many_RN = divmod(arabic_numeral, denominator)
        for num in range(how_many_RN[0]):
            RN_list.append(roman_dictionary[denominator])
        arabic_numeral = how_many_RN[1]  # #15
    RN_joined = ''.join(RN_list)
RN_format_dic = {'CCCC' : ['D', 'CM', 'CD', 'DCCCC'], 'XXXX' : ['L', 'XC', 'XL', 'LXXXX'], 'IIII' : ['V', 'IX', 'IV',
                                                                                                     'VIIII']}
for RN_unformatted in RN_format_dic.keys():
    if RN_unformatted in RN_joined:
        if RN_format_dic[RN_unformatted][0] in RN_joined:
            RN_joined = RN_joined.replace(RN_format_dic[RN_unformatted][3], RN_format_dic[RN_unformatted][1])
        else:
            RN_joined = RN_joined.replace(RN_unformatted, RN_format_dic[RN_unformatted][2])

print(RN_joined)
