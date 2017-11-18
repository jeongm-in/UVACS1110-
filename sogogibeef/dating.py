# version : Jeong Min (sogogibeef)
# dating.py prompts user to input their age and prints
# range of ages of people they can date following below rules.
# as young as half your age plus 7
# as old as twice your age minus 13


# Plus
def date_age_range_calculator():
    user_age = int(input('How old are you? '))
    # Note to self : Apparently input returns string value.
    # In python 2, input automatically chose data type for fed value
    # and raw_input cast every input to string.
    # In python 3, raw_input is removed and input has behavior of raw_input.
    # Thus return value of input function should be cast to whichever data Type
    # Source : https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-integers

    while user_age < 14:
        print('Error; You should be older than 13. ', end='')
        user_age = int(input('How old are you? '))

    return user_age


def age_limit_calculator(age_of_user):
    date_lower_limit = age_of_user / 2 + 7
    date_upper_limit = age_of_user * 2 - 13
    final_line = 'You can date people between {} and {} years old.'.format(date_lower_limit, date_upper_limit)
    # Strange behavior observed :
    # date_lower_limit is float and date_upper_limit is int
    # what????

    print(final_line)


your_age = date_age_range_calculator()
age_limit_calculator(your_age)
