# jeongm(limjeongmin@wustl.edu)
# matchmaker.py contains a collection of functions that will help suer to find compatibility between various things


def agreement(i1, i2):
    result = []
    for item in i1:
        if item in i2:
            result.append(item)
    return result


# print(agreement(['games', 'museums', 'food'], ['art', 'food', 'hiking', 'games']))

def disagreement(i1, i2):
    i1_copy = i1[:]
    i2_copy = i2[:]
    for item in i1:
        if item in i2_copy:
            i1_copy.remove(item)
            i2_copy.remove(item)
    return i1_copy + i2_copy


# print(disagreement(['games', 'museums', 'food'], ['art', 'food', 'hiking', 'games']))

def compatibility(i1, i2):
    # shared / (shared + not shared)
    shared = len(agreement(i1, i2))
    not_shared = len(disagreement(i1, i2))
    result = shared / (shared + not_shared)
    return result


# print(compatibility(['games', 'museums', 'food'], ['art', 'food', 'hiking', 'games']))

def bestmatch(me, others):
    """Returns a most-compatible person, breaking ties with the first person tied.

    Parameters:
        me:     a list of things I like

        others: a list of pairs, where each pair is a name
                and a list of things that person likes; for example,
                [ ["Scrooge", ["money", "food"]],
                  ["Cratchit", ["family", "heat", "food"]]
                ]
    """
    whom = 'no one'
    comp = -1
    for person in others:
        name, likes = person
        match = compatibility(me, likes)
        if match > comp:
            comp = match
            whom = name
    return whom
