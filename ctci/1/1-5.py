'''
One Away:
There are three types of edits that can be performed on strings:
Insert a character
Remove a character
Replace a character

Given two strings, write a function to check if they are <= 1 edit away.
'''
import unittest

class Test(unittest.TestCase):
    str1 = ('pale')
    str2 = ('ple')
    str3 = ('pales')
    str4 = ('bale')
    str5 = ('bake')
    str6 = ('palebo')

    def test_oneaway(self):
        self.assertTrue(one_away(self.str1, self.str2))
        self.assertTrue(one_away(self.str3, self.str1))
        self.assertTrue(one_away(self.str1, self.str4))
        self.assertFalse(one_away(self.str1, self.str5))
        self.assertFalse(one_away(self.str4, self.str6))

def one_away(s1, s2):
    if s1 == s2: return True
    elif abs(len(s1) - len(s2)) > 1: return False
    elif abs(len(s1) - len(s2)) == 1:
        shorter = True
        # ensure s1 is largest string to simplify life
        if len(s1) < len(s2): s1, s2 = s2, s1 
    else:
        shorter = False
    i, j = 0, 0
    diff = False

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            if diff:
                return False
        
            diff = True
            i += 1
            if not shorter:
                j += 1
    return True

if __name__ == "__main__":
    unittest.main()
