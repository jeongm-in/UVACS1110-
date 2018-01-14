def agreement(i1, i2):
    return [x for x in i1 if x in i2]


def disagreement(i1, i2):
    return [x for x in i1 if x not in i2] + [x for x in i2 if x not in i1]


def compatibility(i1, i2):
    # assumes i1 or i2 is nonempty
    return len(agreement(i1, i2)) / \
           len((agreement(i1, i2) + disagreement(i1, i2)))


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
