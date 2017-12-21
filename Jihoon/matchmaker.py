import unittest


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


class TestMatchmaker(unittest.TestCase):
    def test_agreement(self):
        i1 = ['seocho', 'gangnam', 'yeoksam']
        i2 = ['yeoksam', 'samseong', 'jamsil']
        self.assertListEqual(agreement(i1, i2), ['yeoksam'])

    def test_disagreement(self):
        i1 = ['seocho', 'gangnam', 'yeoksam']
        i2 = ['yeoksam', 'samseong', 'jamsil']
        self.assertListEqual(disagreement(i1, i2),
                             ['seocho', 'gangnam', 'samseong', 'jamsil'])

    def test_compatibility(self):
        i1 = ['seocho', 'gangnam', 'yeoksam']
        i2 = ['yeoksam', 'samseong', 'jamsil']
        self.assertEqual(compatibility(i1, i2), .2)

    def test_bestmatch(self):
        me = ['coding', 'homework', 'money', 'reciting poetry']

        k = ['homework']
        m = ['coding', 'homework', 'sleep']
        d = ['money', 'cruises', 'reciting poetry', 'gardening']

        match = bestmatch(me, [['K.', k], ['M.', m], ['D.', d]])
        self.assertEqual(match, 'M.')

    def test_first_three_with_tuples(self):
        a = ('gam', 'nyong', 'jock')
        b = ('ting', 'nyong', 'gam')
        self.assertListEqual(agreement(a, b), ['gam', 'nyong'])
        self.assertListEqual(disagreement(a, b), ['jock', 'ting'])
        self.assertEqual(compatibility(a, b), .5)

    def test_first_three_with_empty_lists(self):
        a = ('gam', 'nyong', 'jock', 'ting')
        b = []
        self.assertListEqual(agreement(a, b), [])
        self.assertListEqual(disagreement(a, b),
                             ['gam', 'nyong', 'jock', 'ting'])
        self.assertEqual(compatibility(a, b), 0)

    def test_first_three_with_same_lists(self):
        a = ('gam', 'nyong', 'jock', 'ting')
        b = ['gam', 'nyong', 'jock', 'ting']
        self.assertListEqual(agreement(a, b),
                             ['gam', 'nyong', 'jock', 'ting'])
        self.assertListEqual(disagreement(a, b), [])
        self.assertEqual(compatibility(a, b), 1)

    def test_first_three_with_mutually_disjoint_lists(self):
        a = ('gam', 'nyong')
        b = ['jock', 'ting']
        self.assertListEqual(agreement(a, b), [])
        self.assertListEqual(disagreement(a, b),
                             ['gam', 'nyong', 'jock', 'ting'])
        self.assertEqual(compatibility(a, b), 0)
