import unittest

from . import crypto as c


class TestCryptography(unittest.TestCase):
    def test_shift_with_given_example1(self):
        self.assertEqual(c.shift('Caesar cipher', 3), 'Fdhvdu flskhu')

    def test_shift_with_given_example2(self):
        self.assertEqual(c.shift('Secret', 9), 'Bnlanc')

    def test_shift_with_all_lowercase_alphabets_and_negative_key(self):
        self.assertEqual(c.shift('abcdefghijklmnopqrstuvwxyz', -25),
                         'bcdefghijklmnopqrstuvwxyza')

    def test_shift_with_non_letters(self):
        self.assertEqual(c.shift("What? That can't be!", 7),
                         "Doha? Aoha jhu'a il!")

    def test_unshift_with_given_example1(self):
        self.assertEqual(c.unshift('Fdhvdu flskhu', 3), 'Caesar cipher')

    def test_unshift_with_given_example2(self):
        self.assertEqual(c.unshift('Bnlanc', 9), 'Secret')

    def test_unshift_with_all_lowercase_alphabets_and_negative_key(self):
        self.assertEqual(c.unshift('bcdefghijklmnopqrstuvwxyza', -25),
                         'abcdefghijklmnopqrstuvwxyz')

    def test_unshift_with_non_letters(self):
        self.assertEqual(c.unshift("Doha? Aoha jhu'a il!", 7),
                         "What? That can't be!")

    def test_vignere_with_given_example(self):
        self.assertEqual(c.vignere('secret', 'hi'), 'zmjzlb')

    def test_vignere_with_uppercase_letter_and_non_letter(self):
        self.assertEqual(c.vignere('X-mas!', 'happy'), 'E-bpq!')

    def test_unvignere_with_given_example(self):
        self.assertEqual(c.unvignere('zmjzlb', 'hi'), 'secret')

    def test_unvignere_with_uppercase_letter_and_non_letter(self):
        self.assertEqual(c.unvignere('E-bpq!', 'happy'), 'X-mas!')

    def test_interleave_with_given_example1(self):
        self.assertEqual(c.interleave('so much fun'), 'sho  fmuunc')

    def test_interleave_with_given_example2(self):
        self.assertEqual(c.interleave('more secretive'), 'mcorreet isvee')

    def test_deinterleave_with_given_example1(self):
        self.assertEqual(c.deinterleave('sho  fmuunc'), 'so much fun')

    def test_deinterleave_with_given_example2(self):
        self.assertEqual(c.deinterleave('mcorreet isvee'), 'more secretive')
