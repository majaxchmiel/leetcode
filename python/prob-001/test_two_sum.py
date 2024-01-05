'''
    https://docs.python.org/3/library/unittest.html
'''

import unittest
from two_sum import TwoSum

class TestTwoSum(unittest.TestCase):
    def testOne(self):
        self.assertEqual(1, 1)

    def testTwo(self):
        self.assertEqual(1, 1)

    def testThree(self):
        self.assertEqual(1, 10)


if __name__ == '__main__':
    unittest.main()