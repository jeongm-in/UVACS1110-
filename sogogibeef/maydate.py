# Version : Jeong Min (sogogibeef)
# maydate.py has a function creepy that takes two people's age
# and returns boolean value whether the two can date without being creepy.


def creepy(person_one_age, person_two_age):
    person_one_upper_limit = int(person_one_age * 2 - 13)
    person_one_lower_limit = int(person_one_age / 2 + 7)
    person_one_datable_range = range(person_one_lower_limit, person_one_upper_limit+1)
    while person_two_age in person_one_datable_range:
        return True
    return False


