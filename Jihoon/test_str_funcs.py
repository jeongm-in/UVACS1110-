import unittest

from . import str_funcs as sf


class TestStringFunctions(unittest.TestCase):
    def test_ellipsis(self, s):
        self.assertEqual(sf.ellipsis('computer science'), 'co..ce')
        self.assertEqual(sf.ellipsis('abcd'), 'abcd')
        self.assertRaises(AssertionError,
                          sf.ellipsis(['ab', 'c', 'd', 'e']))
        self.assertRaises(AssertionError, sf.ellipsis('a'))
        self.assertRaises(AssertionError, sf.ellipsis(''))
        self.assertRaises(AssertionError, sf.ellipsis(12345))

    def test_eighteen(self, s):
        self.assertEqual(sf.eighteen('computer science'), 'c14e')
        self.assertEqual(sf.eighteen('is'), 'i0s')
        self.assertEqual(sf.eighteen('fun'), 'f1n')
        self.assertRaises(AssertionError, sf.eighteen([1, 2, 3, '4']))
        self.assertRaises(AssertionError, sf.eighteen('a'))
        self.assertRaises(AssertionError, sf.eighteen(''))
        self.assertRaises(AssertionError, sf.eighteen(1234))

    def test_allit(self, s, t):
        """True if s and t start with the same non-vowel character
        Your code should treat upper- and lower-case letters as the same."""
        self.assertTrue(sf.allit('hi', 'hello'))
        self.assertTrue(sf.allit('Hi', 'hello'))
        self.assertTrue(sf.allit('jeongmin', 'Jihoon'))
        self.assertFalse(sf.allit('fun', 'great fun'))
        self.assertFalse(sf.allit('exciting', 'excitement'))
        self.assertRaises(AssertionError, sf.allit(['h', 'i'], 'hi'))

    def test_between(self):
        self.assertEqual(sf.between('peripatetics', 'p'), 'eri')
        self.assertEqual(sf.between('loan me a lovely loon to look at',
                                    'lo'), 'an me a ')
        self.assertEqual(sf.between('loan me a lovely loon to look at',
                                    ' lo'), 'vely')
        self.assertEqual(sf.between('quick', 'u'), '')
        self.assertEqual(sf.between('quick', 'z'), '')
        self.assertEqual(sf.between('quick', ''), '')
        self.assertRaises(AssertionError, sf.between([1, 2, 1], 1))
        self.assertRaises(AssertionError,
                          sf.between(['a', 'b', 'a'], 'a'))
        self.assertEqual(sf.between('aa', 'a'), '')
        self.assertEqual(sf.rbetween('abaabaaab', 'a'), 'b')
        self.assertEqual(sf.rbetween('abaabaaab', 'b'), 'aa')

    def test_rbetween(self):
        self.assertEqual(sf.rbetween('peripatetics', 'p'), 'eri')
        self.assertEqual(sf.rbetween('loan me a lovely loon to look at',
                                     'lo'), 'on to ')
        self.assertEqual(sf.rbetween('loan me a lovely loon to look at',
                                     ' lo'), 'on to')
        self.assertEqual(sf.rbetween('quick', 'u'), '')
        self.assertEqual(sf.rbetween('quick', 'z'), '')
        self.assertEqual(sf.rbetween('quick', ''), '')
        self.assertRaises(AssertionError, sf.rbetween([1, 2, 1], 1))
        self.assertRaises(AssertionError,
                          sf.rbetween(['a', 'b', 'a'], 'a'))
        self.assertEqual(sf.rbetween('aa', 'a'), '')
        self.assertEqual(sf.rbetween('abaabaaab', 'a'), '')
        self.assertEqual(sf.rbetween('abaabaaab', 'b'), 'aaa')

    def test_rand_between(self):
        test_cases = [
            ('loan me a lovely loon to look at', 'lo'),
            ('abaabaaab', 'a'),
            ('abaabaaab', 'b'),
        ]
        for test_case in test_cases:
            normal = sf.between(*test_case)
            reversed = sf.rbetween(*test_case)
            random = sf.rand_between(*test_case)
            self.assertIn(random, [normal, reversed])

    def test_temperature(self):
        self.assertEqual(sf.temperature(
            '<p class="myforecast-current-lrg">83&deg;F</p>'), '83')
        self.assertEqual(sf.temperature(
            '<p class="myforecast-current">Fair</p>\n<p class="myforecast-current-lrg">103&deg;F</p><p class="myforecast-current-sm">28&deg;C</p>')
            , "103")

    def test_unhide(self):
        self.assertEqual(sf.unhide('mst3k@virginia.edu'),
                         'mst3k@virginia.edu')
        self.assertEqual(sf.unhide('mst3k at virginia.edu'),
                         'mst3k@virginia.edu')
        self.assertEqual(sf.unhide('mst3k (at) virginia (dot) edu'),
                         'mst3k@virginia.edu')
        self.assertEqual(sf.unhide('mst3k AT virginia DOT edu'),
                         'mst3k@virginia.edu')
        self.assertEqual(sf.unhide('mst3k@virginia dot edu'),
                         'mst3k@virginia.edu')

    def test_vowel_confusion(self):
        self.assertEqual(sf.vowel_confusion("Electric slide"), "Ilictrec sledi")
        self.assertEqual(
            sf.vowel_confusion(
                "I sang, and thought I sang very well; but he just looked up into my face with a very quizzical expression, and said, 'How long have you been singing, Mademoiselle?'"),
            "E sang, and thought E sang viry will; but hi just lookid up ento my faci weth a viry quezzecal ixprisseon, and saed, 'How long havi you biin sengeng, Madimoesilli?'")
        self.assertRaises(AssertionError, sf.vowel_confusion(['e', 'i']))
        self.assertEqual(sf.vowel_confusion('EeIi iIeE'), 'IiEe eEiI')
