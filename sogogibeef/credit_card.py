# check accepts a positive integer input, and returns True if the input is a valid credit card number.


# Form a sum of every other digit, including the right-most digit;
# so 5490123456789128 (5490123456789128) sums to 4 + 0 + 2 + 4 + 6 + 8 + 1 + 8 = 33.
# Double each remaining digit, then sum all the digits that creates it;
# the remaining digits (5 9 1 3 5 7 9 2) in our example (5490123456789128)
# double to 10 18 2 6 10 14 18 4, which sums to 1+0 + 1+8 + 2 + 6 + 1+0 + 1+4 + 1+8 + 4 = 37
# Add the two sums above (33 + 37 = 70)
# If the result is a multiple of 10 (i.e., its last digit is 0) then it was a valid credit card number.

def check(your_credit_card_number):
    credit_card_string = str(your_credit_card_number)
    credit_card_digit_length = len(credit_card_string)
    odd_digits_sum = 0
    even_digits_sum = 0
    print(credit_card_digit_length)

    if credit_card_digit_length % 2 == 0:
        print('even')
        for i in range(credit_card_digit_length):
            if i % 2 == 0:
                even_digits_sum += int(credit_card_string[i])
            else:
                odd_digits_sum += 2 * int(credit_card_string[i])
    else:
        print('odd')
        for i in range(credit_card_digit_length):
            if i % 2 == 0:
                odd_digits_sum += int(credit_card_string[i])
            else:
                even_digits_sum += 2 * int(credit_card_string[i])



    print('odd sum')
    print(odd_digits_sum)
    print('even sum')
    print(even_digits_sum)
    print('sums')
    test_digits_sum = odd_digits_sum + even_digits_sum
    print(test_digits_sum)
    if test_digits_sum % 10 == 0:
        return True
    else:
        return False



if check(5490123456789128):
   print('is valid')
