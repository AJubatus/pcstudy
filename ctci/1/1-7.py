'''
Rotate Matrix:

Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees.

Can you do this in place?
'''
import unittest

class Test(unittest.TestCase):
    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
        
    r1 = [[7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]]

'''
obv there's a pattern here, so let's enumerate the changes

m[0][0] = r[0][2]
m[0][1] = r[1][2]
m[0][2] = r[2][2]
m[1][0] = r[0][1]
m[1][1] = r[1][1]
m[1][2] = r[2][2]
m[2][0] = r[0][0]
m[2][1] = r[1][2]
m[2][2] = r[2][0]

Learned I could use zip() here, should use it more often.
Zip takes in a number of iterables and aggregates them
the ith element of each iterable will be aggregated

here, that works by combining the 0th element, 1th element, and 2nd element from each list (row)

1, 4, 7
2, 5, 8
3, 6, 9

so we reverse the order of the rows

7 8 9
4 5 6
1 2 3

then zip each row

7 4 1
8 5 2
9 6 3

to rotate CCW, we can reverse the rows after zipping, instead of before

1 2 3
4 5 6
7 8 9

becomes

1 4 7
2 5 8
3 6 9

which when reversed becomes

3 6 9
2 5 8
1 4 7
'''

def test_oneaway(self):
    self.assertEqual(self.r1, rotate(self.m1))

def rotate(m):
    return [list(x)[::-1] for x in zip(*m)]

if __name__ == "__main__":
    unittest.main()
