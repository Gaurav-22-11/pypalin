import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("radar"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_is_palindrome_mixed_case(self):
        self.assertTrue(is_palindrome("Able , was I saw eLba"))
