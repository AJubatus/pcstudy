'''
Palindrome Permutation:
Given a string, write a function to check if it is a permutation
of a palindrome.
'''
import unittest
from collections import defaultdict

class Test(unittest.TestCase):
    str1 = ('tact coa')
    str2 = ('car race')
    str3 = ('test')

    def test_permutation(self):
        self.assertTrue(palindrome_permutation(self.str1))
        self.assertTrue(palindrome_permutation(self.str2))
        self.assertFalse(palindrome_permutation(self.str3))

def palindrome_permutation(s):
    count = defaultdict(int)
    for char in s:
        if char != ' ': # ignore space since example ignores them
            count[char] += 1
    # if all character counts are even except one, it can make a palindrome
    odd = list(filter(lambda x: x % 2, count.values()))
    return len(odd) <= 1

        


if __name__ == "__main__":
    unittest.main()
