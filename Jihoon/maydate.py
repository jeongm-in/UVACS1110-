def creepy(age1, age2):
    """Returns False if the two may date each other without being creepy

    Definition of creepy: https://cs1110.cs.virginia.edu/pa03-dating.html

    works for both age orders and fractional ages"""
    younger = min(age1, age2)
    older = max(age1, age2)
    # no need for parentheses below. See https://stackoverflow.com/a/16679309
    return younger < older / 2 + 7


def creepy_permissive(age1, age2):
    """Allows people to date ±1 year even if they are under 16.
    Otherwise, follow the previous rule."""
    if age1 < 16 and age2 < 16 and abs(age1 - age2) <= 1:
        return False
    else:
        return creepy(age1, age2)
