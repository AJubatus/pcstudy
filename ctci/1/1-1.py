# is unique: Implement an algorith to determine if a string has all unique characters
# what if you cannot use additional data structures?
import unittest

class Test(unittest.TestCase):
    str1 = 'abcdefghijkl'
    str2 = 'abcdefghijka'
    str3 = ''

    def test_unique(self):
        self.assertTrue(is_unique(self.str1))
        self.assertFalse(is_unique(self.str2))
        self.assertTrue(is_unique(self.str3))

def is_unique(s):
    s = sorted(s) # creates a list, an additional data structure :(
    for i, char in enumerate(s):
        if i < len(s) - 1:
            if char == s[i+1]:
                return False
    return True

# Alternative approaches:
# Keep a set of encountered characters, return false if char in set
# Convert list to set, compare lengths

if __name__ == "__main__":
    unittest.main()