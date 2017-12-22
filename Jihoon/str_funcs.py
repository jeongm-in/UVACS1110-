import random
import string


def ellipsis(s):
    """replaces all but the first two and last two characters of a string
    with an ellipsis."""
    assert isinstance(s, str), 'Parameter must be a string.'
    assert len(s) > 4, 'Parameter must be more than 4 characters long.'
    return s[:2] + '..' + s[-2:]


def eighteen(s):
    """When internationalization of computer applications became a topic of
    interest, people got tired of typing internationalization so they
    shortened it to i18n, meaning an i, 18 more letters, and then an n.
    This function uses the same idea to shorten any string."""
    assert isinstance(s, str), 'Parameter must be a string.'
    assert len(s) >= 2, 'Parameter must be at least 2characters long.'
    return s[0] + str(len(s) - 2) + s[-1]


def allit(s, t):
    """True if s and t start with the same non-vowel character.
    Your code should treat upper- and lower-case letters as the same."""
    assert isinstance(s, str) and len(s) > 0, \
        "Parameter 's' must be a nonempty string."
    assert isinstance(t, str) and len(t) > 0, \
        "Parameter 't' must be a nonempty string."
    return s[0].lower() == t[0].lower() and t[0].lower() not in 'aeiou'


def between(s, t):
    """returns the portion of its first parameter that falls between the
    first and second occurrence of its second parameter; or return the empty
    string if the second parameter does not occur twice."""
    assert isinstance(s, str), "Parameter 's' must be a string."
    assert isinstance(t, str) and len(t) > 0, \
        "Parameter 't' must be a nonempty string."
    length = len(t)
    if t in s:
        first = s.find(t)
        if t in s[first + length:]:
            second = s[first + length:].find(t)
            return s[first + length:first + length + second]
    return ''


def rbetween(s, t):
    """does the same as between, but looks between the last two, not first
    two, occurrences."""
    assert isinstance(s, str), "Parameter 's' must be a string."
    assert isinstance(t, str) and len(t) > 0, \
        "Parameter 't' must be a nonempty string."
    return between(s[::-1], t[::-1])[::-1]


def rand_between(s, t):
    """randomly does either between or rbetween."""
    random_integer = random.randint(1, 10)
    if random_integer % 2 == 0:
        return between(s, t)
    else:
        return rbetween(s, t)


def temperature(s):
    chunk_before = 'class="myforecast-current-lrg">'
    chunk_after = '&deg;F'
    index_before = s.find(chunk_before)
    index_after = s.find(chunk_after)
    return s[index_before + len(chunk_before):index_after]


def unhide(s):
    """Sometimes people obscure email addresses by writing the @ and . as at
    and dot. This function converts these back to @ and .. Even do this if they
    use capitals or parentheses."""
    s = s.replace(' at ', '@').replace(' dot ', '.')
    s = s.replace(' (at) ', '@').replace(' (dot) ', '.')
    s = s.replace(' AT ', '@').replace(' DOT ', '.')
    return s


def vowel_confusion(s):
    """swaps all e's and i's"""
    assert isinstance(s, str), 'Parameter must be a string.'
    unused = ''
    for character in string.printable:
        if character not in s:
            unused = character
            break
    s = s.replace('e', unused).replace('i', 'e').replace(unused, 'i')
    s = s.replace('E', unused).replace('I', 'E').replace(unused, 'I')
    return s
