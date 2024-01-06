'''
    - assertEqual()
    - assertTrue()
    - assertFalse()
    - assertRaises()
'''

import unittest
from two_sum import TwoSum

class TestTwoSum(unittest.TestCase):
    def testOne(self):
        two_sum = TwoSum()
        a = two_sum.solution_one([2,7,11,15], 9)
        self.assertEqual(a, [0, 1])

    def testTwo(self):
        self.assertEqual(1, 1)

    def testThree(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()