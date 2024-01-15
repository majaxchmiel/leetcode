from typing import List

class TwoSum:
    def solution_0(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            x = target - i
            if x in nums and (nums.index(i) != nums.index(x)):
                return [nums.index(i), nums.index(x)]

    def solution_1(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute force

        Loop through each element x and find if there is another value that
        equals to target - x. 
        '''
    
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
                
    

        """
        for i, num_one in enumerate(nums):
            # num_one = nums[i]
            for j, num_two in enumerate(nums[i+1:]):
                if num_one + num_two == target:
                    return [i, j]
        """
        