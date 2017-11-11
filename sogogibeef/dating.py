# version : Jeong Min (sogogibeef)
# dating.py prompts user to input their age and prints
# range of ages of people they can date following below rules.
# as young as half your age plus 7
# as old as twice your age minus 13


# plus
def date_age_range_calculator():
    user_age = input('How old are you? ') # apparently input returns string value.
    user_age_in_int = int(user_age) # casts user_age String data type to integer data type
    if user_age_in_int < 14:
        print('Error; You should be older than 13. ', end='')
        date_age_range_calculator()
        # Q: what is general opinion on calling a function within itself?
        # Is this even recursion in the first place?
        # When I prompt error message and input expected age, calculation breaks.
        # Should check again here later.

    return user_age_in_int

def age_limit_calculator(age_of_user):
    date_lower_limt = age_of_user / 2 + 7
    date_upper_limit = age_of_user * 2 - 13
    print('You can date people between %d and %d years old' % (date_lower_limt, date_upper_limit), end='\n')


your_age = date_age_range_calculator()
age_limit_calculator(your_age)




