# jeongm(Jeong-Min Lim, limjeongmin@wustl.edu)
# string functions lab
# I will skip assertRaises

def ellipsis(s):
    # Replaces all but the first two and last two characters of a string with an ellipsis (...).
    return s[0:2] + '...' + s[-2:]


def eighteen(s):
    # Returns length of string between first and last character
    return s[0] + str(len(s) - 2) + s[-1]


def allit(s, t):
    # Returns boolean value if both strings begin with same consonant
    return s.lower()[0] == t.lower()[0] and s.lower[0] not in 'aeiou'


def between(s, t):
    '''
    Returns the portion of its first parameter that falls between the first and second occurrence
    of its second parameter; or return the empty string if the second parameter does not occur twice.
    '''
    first = s.find(t) + len(t)
    if t in s[first:]:
        second = s[first:].find(t) + first
        return s[first:second]
    else:
        return ""


def rbetween(s, t):
    '''
    Returns the portion of its first parameter that falls between the first and second occurrence
    of its second parameter; or return the empty string if the second parameter does not occur twice.
    Searches from the back.
    '''
    first = s.rfind(t)
    if t in s[:first - 1]:
        second = s[:first - 1].rfind(t) + len(t)
        return s[second:first]
    else:
        return ""


def rand_between(s, t):
    import random
    if random.randint(0, 1) > 0:
        between(s, t)
    else:
        rbetween(s, t)


def temperature(s):
    # "<p class="myforecast-current-lrg">83&deg;F</p>")
    lrg = 'class="myforecast-current-lrg">'
    deg = '&deg;F'
    lrg_index = s.find(lrg) + len(lrg)
    deg_index = s.find(deg)
    degree = s[lrg_index:deg_index]
    return degree

def unhide(s):
    # Converts at and dot as @ and . , even if those are in Capital or Parentheses
    s = s.replace(' dot ', '.').replace(' at ', '@')
    s = s.replace(' DOT ', '.' ).replace(' AT ', '@')
    s = s.replace(' (dot) ', '.').replace(' (at) ', '@')
    return s


def vowel_confusion(s):
    s = s.replace('I', 'ㄱ').replace('i', 'ㄴ')
    s = s.replace('E', 'I').replace('e', 'i')
    s = s.replace('ㄱ','E').replace('ㄴ','e')
    return s

