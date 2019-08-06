'''
URLify: 
Write a method tp replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end
to hold the additional characters, and that you are given the "true"
length of the string.
'''
import unittest

class Test(unittest.TestCase):
    str1 = ('Mr John Smith    ', 13)
    str2 = ('blah blah blah', 14)
    str3 = ('Mr John Smith    ', 14)

    def test_permutation(self):
        self.assertEqual(len(urlify(self.str1)), 17)
        self.assertEqual(len(urlify(self.str2)), 18)


# doesn't clarify if we remove trailing spaces, so we'll do that
def urlify(s):
    elems = s[0].split()
    URL = '%20'.join(elems)
    return URL

if __name__ == "__main__":
    unittest.main()
