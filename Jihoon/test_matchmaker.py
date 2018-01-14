import itertools
import unittest

from . import matchmaker as mm


def real_perm(some_iterable):
    """The function 'permutation' in the built-in library 'itertools' casts the
    parameter to tuple and returns a generator of tuples. However, this function
    keeps the type of the parameter, albeit inefficiently."""
    iterable_type = type(some_iterable)
    return [iterable_type(x) for x in itertools.permutations(some_iterable)]


class TestMatchmaker(unittest.TestCase):
    def test_agreement_with_given_example(self):
        i1 = ['games', 'museums', 'food']
        i2 = ['art', 'food', 'hiking', 'games']
        self.assertIn(mm.agreement(i1, i2), real_perm(['food', 'games']))

    def test_agreement_with_empty_list(self):
        a = ['gam', 'nyong', 'jock', 'ting']
        b = []
        self.assertListEqual(mm.agreement(a, b), [])

    def test_agreement_with_same_lists(self):
        a = ['gam', 'nyong', 'jock', 'ting']
        self.assertIn(mm.agreement(a, a), real_perm(a))

    def test_agreement_with_mutually_disjoint_lists(self):
        a = ['gam', 'nyong']
        b = ['jock', 'ting']
        self.assertListEqual(mm.agreement(a, b), [])

    def test_disagreement_with_given_example(self):
        i1 = ['games', 'museums', 'food']
        i2 = ['art', 'food', 'hiking', 'games']
        self.assertIn(mm.disagreement(i1, i2),
                      real_perm(['museums', 'art', 'hiking']))

    def test_disagreement_with_empty_list(self):
        a = ['gam', 'nyong', 'jock', 'ting']
        b = []
        self.assertIn(mm.disagreement(a, b), real_perm(a))

    def test_disagreement_with_same_lists(self):
        a = ['gam', 'nyong', 'jock', 'ting']
        self.assertListEqual(mm.disagreement(a, a), [])

    def test_disagreement_with_mutually_disjoint_lists(self):
        a = ['gam', 'nyong']
        b = ['jock', 'ting']
        added = a + b
        self.assertIn(mm.disagreement(a, b), real_perm(added))

    def test_compatibility_with_given_example(self):
        i1 = ['games', 'museums', 'food']
        i2 = ['art', 'food', 'hiking', 'games']
        self.assertEqual(mm.compatibility(i1, i2), .4)

    def test_compatibility_with_empty_list(self):
        a = ['gam', 'nyong', 'jock', 'ting']
        b = []
        self.assertEqual(mm.compatibility(a, b), 0)

    def test_compatibility_with_same_lists(self):
        a = ['gam', 'nyong', 'jock', 'ting']
        self.assertEqual(mm.compatibility(a, a), 1)

    def test_compatibility_with_mutually_disjoint_lists(self):
        a = ['gam', 'nyong']
        b = ['jock', 'ting']
        self.assertEqual(mm.compatibility(a, b), 0)

    def test_bestmatch_with_given_example(self):
        me = ['coding', 'homework', 'money', 'reciting poetry']

        k = ['homework']
        m = ['coding', 'homework', 'sleep']
        d = ['money', 'cruises', 'reciting poetry', 'gardening']

        match = mm.bestmatch(me, [['K.', k], ['M.', m], ['D.', d]])
        self.assertEqual(match, 'M.')
