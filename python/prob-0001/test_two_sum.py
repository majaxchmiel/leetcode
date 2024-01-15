'''
    - assertEqual()
    - assertTrue()
    - assertFalse()
    - assertRaises()
'''

import unittest
from two_sum import TwoSum

class TestTwoSum(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.two_sum = TwoSum()

    def testOne(self):
        nums = [2, 7, 11, 15]
        target = 9

        solution = self.two_sum.solution_1(nums, target)
        expected = [0, 1]
        self.assertEqual(solution, expected)

    def testTwo(self):
        nums = [3, 2, 4]
        target = 6

        solution = self.two_sum.solution_1(nums, target)
        expected = [1, 2]
        self.assertEqual(solution, expected)

    def testThree(self):
        nums = [3, 3]
        target = 6

        solution = self.two_sum.solution_1(nums, target)
        expected = [0, 1]
        self.assertEqual(solution, expected)


if __name__ == '__main__':
    unittest.main()