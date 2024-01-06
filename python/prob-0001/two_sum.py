from typing import List

class TwoSum:
    def solution_one(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute force
        '''
        
        for a in nums:
            b = target - a
            if b in nums and (nums.index(a) != nums.index(b)):
                return [nums.index(a), nums.index(b)]

        return []
        