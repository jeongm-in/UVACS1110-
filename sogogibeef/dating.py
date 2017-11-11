# version : Jeong Min (sogogibeef)
# dating.py prompts user to input their age and prints
# range of ages of people they can date following below rules.
# as young as half your age plus 7
# as old as twice your age minus 13



user_age = input('How old are you? ')
# apparently input returns string value.
user_age_in_int = int(user_age) #casts user_age String data type to integer data type
date_lower_limt = user_age_in_int / 2 + 7
date_upper_limit = user_age_in_int * 2 - 13

print('You can date people between %d and %d years old' % (date_lower_limt, date_upper_limit))



