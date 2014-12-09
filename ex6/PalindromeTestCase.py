import unittest

import palindrome
# import balanced_brackets


class PalindromeTestCase(unittest.TestCase):
    def test_is_palindrome_1(self):
        self.assertTrue(palindrome.is_palindrome_1("141"),
                        "returned false for 141")
        self.assertFalse(palindrome.is_palindrome_1("143"),
                         "returned true for 143")
        self.assertTrue(palindrome.is_palindrome_1(""),
                        "returned false for empty string")
        self.assertTrue(palindrome.is_palindrome_1("a"),
                        "returned false for a")
        self.assertTrue(palindrome.is_palindrome_1("aabbcbbaa"),
                        "returned false for aabbcbbaa")
        self.assertFalse(palindrome.is_palindrome_1("aabbcbbca"),
                         "returned true for aabbcbbca")

    def test_is_palindrome_2(self):
        self.assertTrue(palindrome.is_palindrome_2("141", 0, 2),
                        "returned false for 141")
        self.assertFalse(palindrome.is_palindrome_2("143", 0, 2),
                         "returned true for 143")
        self.assertTrue(palindrome.is_palindrome_2("", 0, 0),
                        "returned false for empty string")
        self.assertTrue(palindrome.is_palindrome_2("a", 0, 0),
                        "returned false for a")
        self.assertTrue(palindrome.is_palindrome_2("aabbcbbaa", 0, 8),
                        "returned false for aabbcbbaa")
        self.assertFalse(palindrome.is_palindrome_2("aabbcbbca", 0, 8),
                         "returned true for aabbcbbca")

                                                
if __name__ == '__main__':
    unittest.main()
