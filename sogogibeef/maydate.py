# Version : Jeong Min (sogogibeef)
# maydate.py has a function creepy that takes two people's age
# and returns boolean value whether the two can date without being creepy.


# def creepy(person_one_age, person_two_age):
#     person_one_upper_limit = int(person_one_age * 2 - 13)
#     person_one_lower_limit = int(person_one_age / 2 + 7)
#     person_one_datable_range = range(person_one_lower_limit, person_one_upper_limit+1)
#     while person_two_age in person_one_datable_range:
#         # Instruction said not to use If statements, so I used while..in statement.
#         # Isn't this but a conditional just like if statement? I didn't use if statement though.
#         return True
#     return False

# Thought question 1: when person_one is younger

# def creepy(person_one_age, person_two_age):
#     person_one_upper_limit = int(person_one_age * 2 - 13)
#     person_one_lower_limit = int(person_one_age / 2 + 7)
#     person_one_datable_range = range(person_one_lower_limit, person_one_upper_limit+1)
#     return person_two_age in person_one_datable_range
#     # This works even when first person is younger. But does not work for fractional ages


# Thought question 2: allow one year age difference
def creepy(person_one_age, person_two_age):
    while (person_one_age and person_two_age < 16) and abs(person_one_age - person_two_age == 1):
        return True
    person_one_upper_limit = int(person_one_age * 2 - 13)
    person_one_lower_limit = int(person_one_age / 2 + 7)
    person_one_datable_range = range(person_one_lower_limit, person_one_upper_limit + 1)
    return person_two_age in person_one_datable_range
