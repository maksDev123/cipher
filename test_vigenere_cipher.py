""" Cipher tesing """
import unittest
from vigenere_cipher import *

class TestShipher(unittest.TestCase):
    """ Tests Shipher """
    def test_shipher_class_creation(self):
        """ Tests shipher class creation"""
        cipher = VigenereCipher("TEST")
        self.assertEqual(cipher.keyword, "TEST")
        cipher = VigenereCipher("test")
        self.assertEqual(cipher.keyword, "TEST")
        self.assertIsInstance(cipher, VigenereCipher)

    def test_extend_keyword(self):
        """ Test keyword extending """
        cipher = VigenereCipher("ABC")
        self.assertEqual(cipher.extend_keyword(3), "ABC")
        self.assertEqual(cipher.extend_keyword(4), "ABCA")
        self.assertEqual(cipher.extend_keyword(10), "ABCABCABCA")
        self.assertEqual(cipher.extend_keyword(1), "A")
        self.assertEqual(cipher.extend_keyword(9), "ABCABCABC")

    def test_combine_character(self):
        """ Test column and row intersection of two letters """

        self.assertEqual(VigenereCipher.combine_character("E", "T"), "X")
        self.assertEqual(VigenereCipher.combine_character("N", "R"),"E")
        self.assertEqual(VigenereCipher.combine_character("A", "B"),"B")

    def test_separate_character(self):
        """ Test separation of two characters first - separation, second - column """
        self.assertEqual(VigenereCipher.separate_character("X", "T"), "E")
        self.assertEqual(VigenereCipher.separate_character("A", "L"), "P")
        self.assertEqual(VigenereCipher.separate_character("K", "E"), "G")


    def test_encode_character(self):
        """ Test letter encoding """
        cipher = VigenereCipher("AAA")
        self.assertEqual(cipher.encode("E"), "E")
        self.assertEqual(cipher.encode("A"), "A")
        self.assertEqual(cipher.encode("c"), "C")

        cipher1 = VigenereCipher("K")
        self.assertEqual(cipher1.encode("E"), "O")
        self.assertEqual(cipher1.encode("A"), "K")
        self.assertEqual(cipher1.encode("c"), "M")

    def test_encode_spaces(self):
        """ Test encoding with spaces """
        cipher = VigenereCipher("TEST")
        self.assertEqual(cipher.encode("S P A C E S"), "LTSVXW")
        self.assertEqual(cipher.encode("spaces "), "LTSVXW")
        self.assertEqual(cipher.encode("SPACES"), "LTSVXW")

    def test_uppercase_encoding(self):
        """ Test uppercase encoding letters """
        cipher = VigenereCipher("TEST")
        self.assertEqual(cipher.encode("TESTENCODING"), "MIKMXRUHWMFZ")
        cipher1 = VigenereCipher("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        self.assertEqual(cipher1.encode("TESTENCODING"), "MXLMXGVHWBGZ")
        cipher3 = VigenereCipher("tetetetetee")
        self.assertEqual(cipher3.encode("TESTENCODING"), "MILXXRVSWMRZ")

    def test_lowercase_encoding(self):
        """ Test lowercase letters encoding """
        cipher = VigenereCipher("TEST")
        self.assertEqual(cipher.encode("testtext"), "MIKMMIPM")
        cipher1 = VigenereCipher("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        self.assertEqual(cipher1.encode("text"), "MXQM")
        cipher3 = VigenereCipher("tetetetetee")
        self.assertEqual(cipher3.encode("eac"), "XEV")

    def test_decode(self):
        """ Test decoding"""
        cipher = VigenereCipher("TEST")
        self.assertEqual(cipher.decode("MIKMMIPM"), "TESTTEXT")
        cipher1 = VigenereCipher("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        self.assertEqual(cipher1.decode("MXQM"), "TEXT")
        cipher3 = VigenereCipher("tetetetetee")
        self.assertEqual(cipher3.decode("XEV"), "EAC")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
