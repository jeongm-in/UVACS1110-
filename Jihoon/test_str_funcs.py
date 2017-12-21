import unittest
from . import str_funcs


class TestStringFunctions(unittest.TestCase):
    def test_ellipsis(self, s):
        self.assertEqual(str_funcs.ellipsis('computer science'), 'co..ce')
        self.assertEqual(str_funcs.ellipsis('abcd'), 'abcd')
        self.assertRaises(AssertionError,
                          str_funcs.ellipsis(['ab', 'c', 'd', 'e']))
        self.assertRaises(AssertionError, str_funcs.ellipsis('a'))
        self.assertRaises(AssertionError, str_funcs.ellipsis(''))
        self.assertRaises(AssertionError, str_funcs.ellipsis(12345))

    def test_eighteen(self, s):
        self.assertEqual(str_funcs.eighteen('computer science'), 'c14e')
        self.assertEqual(str_funcs.eighteen('is'), 'i0s')
        self.assertEqual(str_funcs.eighteen('fun'), 'f1n')
        self.assertRaises(AssertionError, str_funcs.eighteen([1, 2, 3, '4']))
        self.assertRaises(AssertionError, str_funcs.eighteen('a'))
        self.assertRaises(AssertionError, str_funcs.eighteen(''))
        self.assertRaises(AssertionError, str_funcs.eighteen(1234))

    def test_allit(self, s, t):
        """True if s and t start with the same non-vowel character
        Your code should treat upper- and lower-case letters as the same."""
        self.assertTrue(str_funcs.allit('hi', 'hello'))
        self.assertTrue(str_funcs.allit('Hi', 'hello'))
        self.assertTrue(str_funcs.allit('jeongmin', 'Jihoon'))
        self.assertFalse(str_funcs.allit('fun', 'great fun'))
        self.assertFalse(str_funcs.allit('exciting', 'excitement'))
        self.assertRaises(AssertionError, str_funcs.allit(['h', 'i'], 'hi'))

    def test_between(self):
        self.assertEqual(str_funcs.between('peripatetics', 'p'), 'eri')
        self.assertEqual(str_funcs.between('loan me a lovely loon to look at',
                                           'lo'), 'an me a ')
        self.assertEqual(str_funcs.between('loan me a lovely loon to look at',
                                           ' lo'), 'vely')
        self.assertEqual(str_funcs.between('quick', 'u'), '')
        self.assertEqual(str_funcs.between('quick', 'z'), '')
        self.assertEqual(str_funcs.between('quick', ''), '')
        self.assertRaises(AssertionError, str_funcs.between([1, 2, 1], 1))
        self.assertRaises(AssertionError,
                          str_funcs.between(['a', 'b', 'a'], 'a'))
        self.assertEqual(str_funcs.between('aa', 'a'), '')
        self.assertEqual(str_funcs.rbetween('abaabaaab', 'a'), 'b')
        self.assertEqual(str_funcs.rbetween('abaabaaab', 'b'), 'aa')

    def test_rbetween(self):
        self.assertEqual(str_funcs.rbetween('peripatetics', 'p'), 'eri')
        self.assertEqual(str_funcs.rbetween('loan me a lovely loon to look at',
                                            'lo'), 'on to ')
        self.assertEqual(str_funcs.rbetween('loan me a lovely loon to look at',
                                            ' lo'), 'on to')
        self.assertEqual(str_funcs.rbetween('quick', 'u'), '')
        self.assertEqual(str_funcs.rbetween('quick', 'z'), '')
        self.assertEqual(str_funcs.rbetween('quick', ''), '')
        self.assertRaises(AssertionError, str_funcs.rbetween([1, 2, 1], 1))
        self.assertRaises(AssertionError,
                          str_funcs.rbetween(['a', 'b', 'a'], 'a'))
        self.assertEqual(str_funcs.rbetween('aa', 'a'), '')
        self.assertEqual(str_funcs.rbetween('abaabaaab', 'a'), '')
        self.assertEqual(str_funcs.rbetween('abaabaaab', 'b'), 'aaa')

    def test_rand_between(self):
        test_cases = [
            ('loan me a lovely loon to look at', 'lo'),
            ('abaabaaab', 'a'),
            ('abaabaaab', 'b'),
        ]
        for test_case in test_cases:
            normal = str_funcs.between(*test_case)
            reversed = str_funcs.rbetween(*test_case)
            random = str_funcs.rand_between(*test_case)
            self.assertIn(random, [normal, reversed])

    def test_temperature(self):
        self.assertEqual(str_funcs.temperature(
            '<p class="myforecast-current-lrg">83&deg;F</p>'),
            '83')
        self.assertEqual(str_funcs.temperature(
            '<p class="myforecast-current">Fair</p>\n<p class="myforecast-current-lrg">103&deg;F</p><p class="myforecast-current-sm">28&deg;C</p>')
            , "103")

    def test_unhide(self):
        self.assertEqual(str_funcs.unhide('mst3k@virginia.edu'),
                         'mst3k@virginia.edu')
        self.assertEqual(str_funcs.unhide('mst3k at virginia.edu'),
                         'mst3k@virginia.edu')
        self.assertEqual(str_funcs.unhide('mst3k (at) virginia (dot) edu'),
                         'mst3k@virginia.edu')
        self.assertEqual(str_funcs.unhide('mst3k AT virginia DOT edu'),
                         'mst3k@virginia.edu')
        self.assertEqual(str_funcs.unhide('mst3k@virginia dot edu'),
                         'mst3k@virginia.edu')

    def test_vowel_confusion(self):
        self.assertEqual(str_funcs.vowel_confusion("Electric slide"),
                         "Ilictrec sledi")
        self.assertEqual(
            str_funcs.vowel_confusion(
                "I sang, and thought I sang very well; but he just looked up into my face with a very quizzical expression, and said, 'How long have you been singing, Mademoiselle?'"),
            "E sang, and thought E sang viry will; but hi just lookid up ento my faci weth a viry quezzecal ixprisseon, and saed, 'How long havi you biin sengeng, Madimoesilli?'")
        self.assertRaises(AssertionError, str_funcs.vowel_confusion(['e', 'i']))
        self.assertEqual(str_funcs.vowel_confusion('EeIi iIeE'), 'IiEe eEiI')
