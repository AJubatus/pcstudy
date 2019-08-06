# check permutation: given two strings, write a method to decide if one is a permutation of the other.
import unittest
from collections import defaultdict

class Test(unittest.TestCase):
    str1 = 'abcdef'
    str2 = 'fabcde'
    str3 = 'abcdefg'
    str4 = ''
    str5 = 'gjdicm'

    def test_permutation(self):
        self.assertTrue(is_permutation(self.str1, self.str2))
        self.assertTrue(is_permutation(self.str1, self.str1))
        self.assertFalse(is_permutation(self.str1, self.str3))
        self.assertFalse(is_permutation(self.str1, self.str4))
        self.assertFalse(is_permutation(self.str1, self.str5))

def is_permutation(s1, s2):
    if len(s1) != len (s2):
        return False
    charmap = defaultdict(int)
    for char in s1:
        charmap[char] += 1
    for char in s2:
        if charmap[char] > 0:
            charmap[char] -= 1
        else:
            return False
    return True

# Alternative approaches:
# Sort both lists, step through both at same time
# Tradeoff, less memory usage but O(n log n) instead of O(n)

if __name__ == "__main__":
    unittest.main()