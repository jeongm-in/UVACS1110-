# jeongm(Jeong-Min Lim, limjeongmin@wustl.edu)
# string functions lab

def ellipsis(s):
    return s[0:2] + '...' + s[-2:]


def eighteen(s):
    return s[0] + str(len(s) - 2) + s[-1]


def allit(s, t):
    return s.lower()[0] == t.lower()[0]


def between(s, t):
    first_occurence = s.find(t) + len(t)
    second_occurence = first_occurence + s[first_occurence:].find(t)
    if s.find(t) == -1 or s[first_occurence:].find(t) == -1:
        return ""
    else:
        return s[first_occurence:second_occurence]


def rbetween(s, t):
    first_occurence = s.rfind('t')
    second_occurence = s[:first_occurence].rfind(t) + len(t)
    if s.rfind(t) == -1 or s[:first_occurence].rfind(t) == -1:
        return ""
    else:
        return s[second_occurence:first_occurence]


print(rbetween('loan me a lovely loon to look at', 'lo'))
